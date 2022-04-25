from pytest import mark
@mark.smoke
def test_validation():
    print("Executing the login test")

@mark.regression
def test_shopping():
    print("Executing the shopping test")

@mark.smoke
def test_payment():
    print("Executing the payment test")

@mark.regression
def test_registration():
    print("Executing the registration test")
