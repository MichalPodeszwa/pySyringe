from pysyringe import inject_value, inject
from pysyringe.tests.stubs import Foo


def test_simple_mix():

    @inject(foo=Foo)
    @inject_value(bar="BAR")
    def test_func(foo, bar):
        return foo, bar

    a, b = test_func()
    assert isinstance(a, Foo)
    assert b == "BAR"
