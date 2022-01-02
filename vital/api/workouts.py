from typing import List, Mapping, Optional

from vital.api.api import API


class Workouts(API):
    """Endpoints for getting sleep data."""

    def get(
        self,
        user_key: str,
        start_date: str,
        end_date: str,
        provider: Optional[str] = "",
    ) -> Mapping[str, List[Mapping]]:
        """
        GET Workout data.
        """
        return self.client.get(
            f"/summary/workouts/{user_key}",
            params={
                "start_date": start_date,
                "end_date": end_date,
                "provider": provider,
            },
            api_version="v2",
        )

    def get_stream(
        self,
        workout_id: str,
    ) -> Mapping:
        """
        GET Workout Stream data.
        """
        return self.client.get(
            f"/timeseries/workouts/{workout_id}/stream", api_version="v2"
        )
