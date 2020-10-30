import unittest

from fastapi.testclient import TestClient

from ..router import router


class TestRouter(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(router)

    def test_post_pharmacies(self):
        """
        post request to /pharmacies route with 
        valid data responds with status 200
        """
        response = self.client.post("/")
        self.assertEqual(response.status_code, 200)

    def test_get_pharmacies(self):
        """get request to /pharmacies responds with status 405"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 405)
