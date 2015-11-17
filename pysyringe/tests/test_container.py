
def test_multiple_getting(container):

    class Foo:
        pass

    foo = container.get_instance(Foo)
    assert id(foo) == id(container.get_instance(Foo))
