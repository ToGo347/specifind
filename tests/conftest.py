import pytest
from specifind import Specifind


@pytest.fixture(scope="session")
def specifind_session():
	return Specifind()
