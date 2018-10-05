import unittest
from api import app
import json


class TestEntryViews(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client

    def test_create_entry(self):
        # Test that an entry is created
        post_data = (
            {
                "entry_text": "my name is mary",
            }
        )
        response = self.client().post('/api/v1/entries',
                                      content_type='application/json',
                                      data=json.dumps(post_data))
        self.assertEqual(response.status_code, 201)

    def test_for_empty_entry_fields(self):
        # Tests response in case of empty fields
        post_data = (
            {
                "entry_text": "",
            }
        )
        response = self.client().post('/api/v1/entries',
                                      content_type='application/json',
                                      data=json.dumps(post_data))
        self.assertEqual(response.status_code, 400)

    def test_fetch_all_entries(self):
        # Tests that the endpoint successfully fetches all rides
        response = self.client().get('/api/v1/entries',
                                     content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_fetch_one(self):
        response = self.client().get('/api/v1/entries/1',
                                     content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_fetch_one_id(self):
        # Tests that the endpoint return invalid status code for wrong indices
        response = self.client().get('/api/v1/entries/0',
                                     content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_invalid_id_in_modify_entry(self):
        # Tests that the response is invalid for invalid id
        response = self.client().put('/api/v1/entries/0',
                                     content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_modify_entry(self):
        # Tests that an entry is modified
        post_data = (
            {
                "entry_text": "this is an update",
            }
        )
        response = self.client().put('/api/v1/entries/1',
                                     content_type='application/json',
                                     data=json.dumps(post_data))
        self.assertEqual(response.status_code, 200)
