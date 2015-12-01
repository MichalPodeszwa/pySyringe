from pysyringe import inject_value


def test_value_injection():

    @inject_value(val="FOO")
    def test_func(val):
        return val

    test_func() == "FOO"
    test_func("MOCKED") == "MOCKED"


def test_multiple_value_injection():

    @inject_value(val="FOO", val2="FOO2")
    def test_func(val, val2):
        return val, val2

    test_func() == "FOO", "FOO2"
    test_func("MOCKED") == "MOCKED", "FOO2"
    test_func("MOCKED", "MOCKED2") == "MOCKED", "MOCKED2"
    test_func(val="MOCKED") == "MOCKED", "FOO2"
    test_func(val2="MOCKED") == "FOO", "MOCKED"
    test_func(val="MOCKED", val2="MOCKED2") == "MOCKED", "MOCKED2"
    test_func("MOCKED", val2="MOCKED") == "FOO", "MOCKED"


def test_chained_value_injection():

    @inject_value(val="FOO")
    @inject_value(val2="FOO2")
    def test_func(val, val2):
        return val, val2

    test_func() == "FOO", "FOO2"
    test_func("MOCKED") == "MOCKED", "FOO2"
    test_func("MOCKED", "MOCKED2") == "MOCKED", "MOCKED2"
    test_func(val="MOCKED") == "MOCKED", "FOO2"
    test_func(val2="MOCKED") == "FOO", "MOCKED"
    test_func(val="MOCKED", val2="MOCKED2") == "MOCKED", "MOCKED2"
    test_func("MOCKED", val2="MOCKED") == "FOO", "MOCKED"
