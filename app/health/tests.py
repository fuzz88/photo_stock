import json

from django.test import TestCase
from django.test import Client

class TestHealthCheck(TestCase):
    def setUp(self):
        self.c = Client()

    def test_is_service_online_route(self):
        resp = self.c.get("/health/")
        self.assertEquals(json.loads(resp.content), {"status": "online"})
