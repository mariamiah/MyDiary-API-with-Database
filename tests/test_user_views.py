import unittest
import json
from api import app


class TestUserViews(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client

    def test_register_user(self):
        # Tests that a  user is registered
        post_data = (
            {
                "user_name": "maria",
                "email": "maria@gmail.com",
                "password": "4567903"
            }
        )
        response = self.client().post('/api/v1/signup',
                                      content_type='application/json',
                                      data=json.dumps(post_data))
        self.assertEqual(response.status_code, 201)

    def test_for_empty_name_fields(self):
        # Tests response in case of empty fields

        post_data = (
            {
                "user_name": "",
                "email": "",
                "password": "rtew"
            }
        )
        response = self.client().post('/api/v1/signup',
                                      content_type='application/json',
                                      data=json.dumps(post_data))
        self.assertEqual(response.status_code, 400)

    def test_get_users(self):
        # Tests that the endpoint successfully fetches users
        response = self.client().get('/api/v1/diaries',
                                     content_type='application/json')
        self.assertEqual(response.status_code, 200)
