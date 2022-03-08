import arrow
import pytest


@pytest.fixture
def start_date():
    return arrow.get().shift(days=-460).isoformat()


@pytest.fixture
def end_date():
    return arrow.get().isoformat()
