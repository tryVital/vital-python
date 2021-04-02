import json
from functools import partial
from json.decoder import JSONDecodeError
from typing import Any, Dict, Mapping, Optional

import requests

from vital.errors import VitalError
from vital.version import __version__

ALLOWED_METHODS = {"post", "get"}
DEFAULT_TIMEOUT = 600  # 10 minutes


def _requests_http_request(
    url: str,
    method: str,
    data: Optional[Mapping],
    headers: Dict,
    timeout: int = DEFAULT_TIMEOUT,
) -> Any:
    normalized_method = method.lower()
    headers.update({"User-Agent": "Vital Python v{}".format(__version__)})
    if normalized_method in ALLOWED_METHODS:
        return getattr(requests, normalized_method)(
            url,
            json=data,
            headers=headers,
            timeout=timeout,
        )
    else:
        raise Exception("Invalid request method {}".format(method))


def _http_request(
    url: str,
    method: str,
    data: Optional[Mapping] = None,
    headers: Dict = {},
    timeout: int = DEFAULT_TIMEOUT,
    is_json: bool = True,
) -> Any:
    response = _requests_http_request(url, method, data, headers or {}, timeout)

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
                response_body.get("detail"), response.status_code
            )
        else:
            return response_body
    else:
        return response.content


# helpers to simplify partial function application
post_request = partial(_http_request, method="POST")
get_request = partial(_http_request, method="GET", data=None)
