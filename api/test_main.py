import unittest

from fastapi.testclient import TestClient


from .main import app


class TestServer(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_index(self):
        """server index route responds with status 404"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 404)
