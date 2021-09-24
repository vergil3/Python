import pytest

def test_devide_by_zero():
    with pytest.raises(ZeroDivisionError):
        1 / 0
