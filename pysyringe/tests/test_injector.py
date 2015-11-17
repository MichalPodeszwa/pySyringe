import pytest

from pysyringe import inject

from .stubs import Foo, Baz, Mocked


@inject(foo=Foo)
@inject(baz=Baz)
def chained_injections(foo, baz):
    return foo, baz


@inject(foo=Foo)
def single_inject(foo):
    return foo, None


@inject(foo=Foo, baz=Baz)
def multi_injections(foo, baz):
    return foo, baz


DEFAULT_TEST_PARAMETERS = [
    (single_inject, False),
    (multi_injections, True),
    (chained_injections, True),
]


@pytest.mark.parametrize("func, should_assert_baz", DEFAULT_TEST_PARAMETERS)
def test_injecting(func, should_assert_baz):
    returned_foo, returned_baz = func()

    assert isinstance(returned_foo, Foo)
    if should_assert_baz:
        assert isinstance(returned_baz, Baz)


@pytest.mark.parametrize("func, should_assert_baz", DEFAULT_TEST_PARAMETERS)
def test_overriding_by_first_kwarg(func, should_assert_baz):
    foo = Mocked()
    returned_foo, returned_baz = func(foo=foo)

    assert foo == returned_foo
    if should_assert_baz:
        assert isinstance(returned_baz, Baz)


@pytest.mark.parametrize("func", [multi_injections, chained_injections])
def test_overriding_by_second_kwarg(func):
    baz = Mocked()
    returned_foo, returned_baz = func(baz=baz)

    assert isinstance(returned_foo, Foo)
    assert baz == returned_baz


@pytest.mark.parametrize("func, should_assert_baz", DEFAULT_TEST_PARAMETERS)
def test_overriding_by_one_arg(func, should_assert_baz):
    foo = Mocked()
    returned_foo, returned_baz = func(foo)

    assert returned_foo == foo
    if should_assert_baz:
        assert isinstance(returned_baz, Baz)


@pytest.mark.parametrize("func", [multi_injections, chained_injections])
def test_overriding_by_two_args(func):
    foo = Mocked()
    baz = Mocked()

    assert foo, baz == func(foo, baz)
