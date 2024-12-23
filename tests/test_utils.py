import pytest

from pyzcode.utils import convert_to_int


def test_convert_to_int():
    assert convert_to_int("123") == 123
    assert convert_to_int(123) == 123
    assert convert_to_int("  456  ") == 456
    with pytest.raises(ValueError):
        convert_to_int("abc")
    with pytest.raises(ValueError):
        convert_to_int("123abc")
    with pytest.raises(ValueError):
        convert_to_int("")
