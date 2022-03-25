import json
from functools import partial
from json.decoder import JSONDecodeError
from typing import Any, Dict, Mapping, Optional

import requests

from vital.errors import VitalError
from vital.version import __version__

ALLOWED_METHODS = {"post", "get", "delete"}
DEFAULT_TIMEOUT = 600  # 10 minutes


def _requests_http_request(
    url: str,
    method: str,
    data: Optional[Mapping],
    headers: Dict,
    timeout: int = DEFAULT_TIMEOUT,
    params: Optional[Mapping] = {},
    session: Optional[requests.Session] = None,
) -> Any:
    normalized_method = method.lower()
    headers.update({"User-Agent": "Vital Python v{}".format(__version__)})
    if normalized_method in ALLOWED_METHODS:
        return getattr(session if session else requests, normalized_method)(
            url, json=data, headers=headers, timeout=timeout, params=params
        )
    else:
        raise Exception("Invalid request method {}".format(method))


def _http_request(
    url: str,
    method: str,
    data: Optional[Mapping] = None,
    headers: Dict = {},
    params: Dict = {},
    timeout: int = DEFAULT_TIMEOUT,
    is_json: bool = True,
    session: Optional[requests.Session] = None,
) -> Any:
    response = _requests_http_request(
        url, method, data, headers or {}, timeout, params=params, session=session
    )

    if is_json or response.headers["Content-Type"] == "application/json":
        try:
            response_body = json.loads(response.text)
        except JSONDecodeError:
            raise VitalError.from_response(
                {
                    "error_message": response.text,
                    "error_type": "API_ERROR",
                    "error_code": "INTERNAL_SERVER_ERROR",
                    "causes": [],
                },
                400,
            )
        if not response.ok:
            raise VitalError.from_response(
                response_body.get("detail", response_body), response.status_code
            )
        else:
            return response_body
    else:
        return response.content


# helpers to simplify partial function application
post_request = partial(_http_request, method="POST")
get_request = partial(_http_request, method="GET", data=None)
delete_request = partial(_http_request, method="DELETE", data=None)
