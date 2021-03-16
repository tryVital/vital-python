from typing import Any
from vital.api.api import API
from typing import Mapping


class SourceSpecific(API):
    """Endpoints for getting source specific data."""

    def get(self, user_id: str, device: str, start_date: str, end_date: str):
        """
        GET Sleep data.
        """
        return self.client.get(
            f"/source_specific/{user_id}/{device}"
            + f"?start_date={start_date}&end_date={end_date}"
        )
