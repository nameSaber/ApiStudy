import pytest
from testcases.conftest import auth_data


@pytest.fixture(scope="function")
def testcase_auth_data(request):
    testcase_name = request.function.__name__
    return auth_data.get(testcase_name)