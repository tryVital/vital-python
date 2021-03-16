from vital.client import Client


class API(object):
    """Base class for classes containing groups of API endpoints."""

    def __init__(self, client: Client):
        self.client = client
