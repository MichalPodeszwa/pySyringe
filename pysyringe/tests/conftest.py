import pytest
from pysyringe.container import IOCContainer


@pytest.fixture
def container(request):
    cont = IOCContainer()

    def cleanup():
        cont._instances = {}
    request.addfinalizer(cleanup)
    return cont
