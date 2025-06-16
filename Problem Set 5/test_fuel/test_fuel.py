from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("4/4") == 100
    assert convert("1/4") == 25
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("1/3") == 33
    assert convert("0/4") == 0
    assert convert("1/100") == 1
    assert convert("99/100") == 99

    with pytest.raises(ValueError):
        convert("cat/dog")

    with pytest.raises(ValueError):
        convert("one/two")

    with pytest.raises(ValueError):
        convert("5/4")

    with pytest.raises(ValueError):
        convert("2.5/5")

    with pytest.raises(ValueError):
        convert("1-4")

    with pytest.raises(ZeroDivisionError):
        convert("2/0")

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"
    assert gauge(25) == "25%"
    assert gauge(75) == "75%"
    assert gauge(98) == "98%"
    assert gauge(2) == "2%"
