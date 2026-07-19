import copy

import pytest
from fastapi.testclient import TestClient

from src import app as app_module


@pytest.fixture(autouse=True)
def reset_app_state():
    app_module.reset_activities()
    yield
    app_module.reset_activities()


@pytest.fixture
def client():
    with TestClient(app_module.app) as test_client:
        yield test_client
