from plates import is_valid

def test_is_valid():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("HELLO") == True
    assert is_valid("GOODBYE") == False
    assert is_valid("123") == False
    assert is_valid("AB2C") == False
    assert is_valid("ABC") == True
    assert is_valid("a") == False
    assert is_valid("ABC!") == False
