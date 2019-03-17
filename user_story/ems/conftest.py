import pytest
@pytest.fixture
def container_url():
	return "https://reqres.in"

@pytest.fixture
def service_url():
	return "https://reqres.in/api"

@pytest.fixture
def context():
    return {}
