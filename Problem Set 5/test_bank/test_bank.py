from bank import value

def test_value():
    assert value("Hello") == 0
    assert value("What's up") == 100
    assert value("Hey") == 20
    assert value("  how are you doing today? ") == 20
    assert value("greetings from Pakistan!") == 100
    assert value(" hello ") == 0
