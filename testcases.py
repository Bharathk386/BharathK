import unittest
import json
from bharathapi import app


class TestAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_sanitized_input(self):
        payload = {'payload': 'bharath'}
        response = self.client.post('/v1/sanitized/input/', json=payload)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['result'], 'sanitized')

    def test_unsanitized_input(self):
        payload = {'payload': 'bharath;'}
        response = self.client.post('/v1/sanitized/input/', json=payload)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['result'], 'unsanitized')


if __name__ == '__main__':
    unittest.main()

