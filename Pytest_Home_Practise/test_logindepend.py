from pytest import mark
@mark.dependency()
def test_login_3():
    print("Logging in")
    assert True

@mark.dependency(depends = ['test_login_3'])
def test_logout():
    print("Logging out")
