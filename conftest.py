"""Configration for pytest to run the test suite"""
import pytest

from api_app.app import create_app

app = create_app()

@pytest.fixture
def client(tmpdir):
    """Create a test client to send requests to"""
    with app.test_client() as c:
        yield c


