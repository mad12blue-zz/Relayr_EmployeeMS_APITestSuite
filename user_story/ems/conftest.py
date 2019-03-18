import pytest

# Container URL of the EMS service
@pytest.fixture
def container_url():
	return "https://reqres.in"

# Service URL of the EMS service
@pytest.fixture
def service_url():
	return "https://reqres.in/api"

# Static variables to be used across methods
@pytest.fixture
def context():
    return {}
