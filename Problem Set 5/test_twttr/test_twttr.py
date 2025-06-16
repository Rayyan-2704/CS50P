from twttr import shorten

def test_shorten():
    assert shorten("AEIOU") == ""
    assert shorten("aeiou") == ""
    assert shorten("cs50p") == "cs50p"
    assert shorten("CS50P") == "CS50P"
    assert shorten("Hello, my name is Rayyan") == "Hll, my nm s Ryyn"
    assert shorten("1234aeo56") == "123456"
    assert shorten("Does he know about the D-O-R-E?") == "Ds h knw bt th D--R-?"
