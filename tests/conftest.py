import pytest
from specifind import Specifind


@pytest.fixture(scope="session", params=[True, False])
def specifind_session(request):
	return Specifind(use_gpu=request.param)
