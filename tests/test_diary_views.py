import unittest
from api import app
import json


class TestDiaryViews(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client

    def test_create_diary(self):
        # Tests that a diary is created
        post_data = (
            {
                "diary_name": "dearestdiary",
            }
        )
        response = self.client().post('/api/v1/diaries',
                                      content_type='application/json',
                                      data=json.dumps(post_data))
        self.assertEqual(response.status_code, 201)

    def test_for_empty_diary_fields(self):
        # Tests response in case of empty fields
        post_data = (
            {
                "diary_name": "",
            }
        )
        response = self.client().post('/api/v1/diaries',
                                      content_type='application/json',
                                      data=json.dumps(post_data))
        self.assertEqual(response.status_code, 400)

    def test_fetch_all_diaries(self):
        # Tests that the endpoint successfully fetches all diaries
        response = self.client().get('/api/v1/diaries',
                                     content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_fetch_one_diary(self):
        response = self.client().get('/api/v1/diaries/1',
                                     content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_fetch_one_diary_id(self):
        # Tests that the endpoint return invalid status code for wrong indices
        response = self.client().get('/api/v1/entries/0',
                                     content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_invalid_id_in_delete_diary(self):
        # Tests that the response is invalid for invalid id
        response = self.client().delete('/api/v1/diaries/0',
                                        content_type='application/json')
        self.assertEqual(response.status_code, 400)
