from fastapi.testclient import TestClient

import unittest

from .main import app

class TestServer(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_index(self):
        """Server index route responds with a status 404"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 404)
