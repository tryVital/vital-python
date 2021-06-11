from vital.api import (
    Activity,
    Body,
    LinkToken,
    ProviderSpecific,
    Sleep,
    Webhooks,
    Workouts,
)
from vital.api.user import User
from vital.internal.requester import (
    DEFAULT_TIMEOUT,
    delete_request,
    get_request,
    post_request,
)
from vital.internal.token_handler import TokenHandler
from vital.internal.utils import urljoin


def get_base_url(environment: str) -> str:
    if environment == "local":
        return "http://localhost:8000"
    if environment == "sandbox" or environment == "dev":
        return "https://api." + environment + ".tryvital.io"
    elif environment == "production" or environment == "prod":
        return "https://api.tryvital.io"
    raise Exception("Environment not supported")


class Client:
    """
    Python Vital API client.
    All of the endpoints documented under the ``vital.api``
    module may be called from a ``vital.Client`` instance.
    """

    def __init__(
        self,
        client_id=None,
        secret=None,
        environment=None,
        timeout=DEFAULT_TIMEOUT,
        api_version="v1",
        **kwargs,
    ):
        """
        Initialize a client with credentials.
        :param  str     client_id:          Your Vital client ID
        :arg    str     secret:             Your Vital secret
        :arg    str     environment:        One of ``sandbox`` or ``production``.
        :arg    int     timeout:            Timeout for API requests.
        """
        self.client_id = client_id
        self.client_secret = secret
        self.environment = environment
        self.timeout = timeout
        self.api_version = api_version
        self.base_url = get_base_url(environment)
        self.token_handler = TokenHandler(
            self.client_id,
            self.client_secret,
            self.environment,
            audience=kwargs.get("audience"),
            domain=kwargs.get("domain"),
        )
        # Mirror the HTTP API hierarchy
        self.LinkToken = LinkToken(self)
        self.Body = Body(self)
        self.Activity = Activity(self)
        self.ProviderSpecific = ProviderSpecific(self)
        self.Sleep = Sleep(self)
        self.User = User(self)
        self.Workouts = Workouts(self)
        self.Webhooks = Webhooks(self)

    def post(self, path, data, is_json=True, params={}):
        """Make a post request."""
        return self._post(path, data, is_json, params)

    def get(self, path, params={}):
        """Make a get request."""
        return self._get(path, params)

    def delete(self, path, params={}):
        """Make a delete request."""
        return self._delete(path, params)

    def post_public(self, path, data, is_json=True):
        """Make a post request requiring no auth."""
        return self._post(path, data, is_json)

    def _post(self, path, data, is_json, params={}):
        headers = {"Authorization": f"Bearer {self.token_handler.access_token}"}
        return post_request(
            urljoin(
                self.base_url,
                f"{self.api_version}{path}",
            ),
            data=data,
            timeout=self.timeout,
            is_json=is_json,
            headers=headers,
            params=params,
        )

    def _get(self, path, params={}):
        headers = {"Authorization": f"Bearer {self.token_handler.access_token}"}
        return get_request(
            urljoin(
                self.base_url,
                f"{self.api_version}{path}",
            ),
            timeout=self.timeout,
            headers=headers,
            params=params,
        )

    def _delete(self, path, params={}):
        headers = {"Authorization": f"Bearer {self.token_handler.access_token}"}
        return delete_request(
            urljoin(
                self.base_url,
                f"{self.api_version}{path}",
            ),
            timeout=self.timeout,
            headers=headers,
            params=params,
        )
