import functions_to_test as functions_to_test

def test_power():
    assert functions_to_test.power(2,2) == 4
    assert functions_to_test.power(2,3) == 8

def test_division():
    assert functions_to_test.division(10,2) == 5
    assert functions_to_test.division(3,2) == 1.5

def test_create_full_name():
    assert functions_to_test.create_full_name("harry","pannekoek") == "harry pannekoek"
    assert functions_to_test.create_full_name("bob","bouwer") == "bob bouwer"

def test_multiply():
    assert functions_to_test.multiply(10,2) == 20
    assert functions_to_test.multiply(2,5) == 10