from starlette.testclient import TestClient

from main import app


class TestCalculationEndpoints:

    # fixture examples
    def test_return_sum(self, test_app): # test_app fixture included
        test_data = {
            "first_val": 10,
            "second_val": 8
        }
        # test_app replaces client
        response = test_app.post("/sum/", json=test_data)

        assert response.status_code == 200
        assert response.json() == 18


    def test_return_difference(self, test_app):
        test_data = {
            "first_val": 10,
            "second_val": 8
        }

        response = test_app.post("/subtract/", json=test_data)

        assert response.status_code == 200
        assert response.json() == 2


    def test_return_product(self, test_app):
        test_data = {
            "first_val": 8,
            "second_val": 2
        }

        response = test_app.post("/multiplication/", json=test_data)

        assert response.status_code == 200
        assert response.json() == 16


    def test_return_dividend(self, test_app):
        test_data = {
            "first_val": 8,
            "second_val": 2
        }

        response = test_app.post("/division/", json=test_data)

        assert response.status_code == 200
        assert response.json() == 4
