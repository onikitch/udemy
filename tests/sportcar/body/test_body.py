from pytest import mark


@mark.body
class BodyTest:
    def test_body_functions_as_expected(self):
        assert True

    def test_bumper(self):
        assert True

    @mark.smoke
    def test_wind(self):
        assert True