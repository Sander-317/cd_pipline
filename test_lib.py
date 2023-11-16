import lib

def test_power():
    assert lib.power(2,2) == 4
    assert lib.power(2,3) == 8

def test_division():
    assert lib.division(10,2) == 5
    assert lib.division(3,2) == 1.5

def test_create_full_name():
    assert lib.create_full_name("harry","pannekoek") == "harry pannekoek"
    assert lib.create_full_name("bob","bouwer") == "bob bouwer"

def test_multiply():
    assert lib.multiply(10,2) == 20
    assert lib.multiply(2,5) == 100