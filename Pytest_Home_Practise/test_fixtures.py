from pytest import fixture
@fixture
def greet():
    return "Hello World"
# Passing the fixture to the Method

def test_greet(greet):
    assert "Hello World" == greet
    