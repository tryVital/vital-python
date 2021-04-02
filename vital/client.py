from vital.api import Activity, Body, LinkToken, ProviderSpecific, Sleep
from vital.api.user import User
from vital.internal.requester import DEFAULT_TIMEOUT, get_request, post_request
from vital.internal.token_handler import TokenHandler
from vital.internal.utils import urljoin


def get_base_url(environment: str) -> str:
    if environment == "sandbox":
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

    def post(self, path, data, is_json=True):
        """Make a post request with client_id and secret key."""
        return self._post(path, data, is_json)

    def get(self, path):
        """Make a post request with client_id and secret key."""
        return self._get(path)

    def post_public(self, path, data, is_json=True):
        """Make a post request requiring no auth."""
        return self._post(path, data, is_json)

    def _post(self, path, data, is_json):
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
        )

    def _get(self, path):
        headers = {"Authorization": f"Bearer {self.token_handler.access_token}"}
        return get_request(
            urljoin(
                self.base_url,
                f"{self.api_version}{path}",
            ),
            timeout=self.timeout,
            headers=headers,
        )
