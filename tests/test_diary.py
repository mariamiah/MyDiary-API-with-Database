import unittest
from api.models import Diary


class TestDiary(unittest.TestCase):
    def setUp(self):
        self.diary = Diary(1, "Food", "Tue, 25 Sep 2018 23:53:50 GMT")

    def test_diary_id(self):
        # Tests that the diary_id is equal to the given diary_id
        self.assertEqual(self.diary.diary_id, 1, "diary_id must be 1")
        self.diary.diary_id = 5
        self.assertEqual(self.diary.diary_id, 5, "diary_id is now 5")

    def test_diary_name(self):
        # Tests that the diary_name is equal to the given diary_name
        self.assertEqual(self.diary.diary_name, "Food")
        self.diary.diary_name = "hello"
        self.assertEqual(self.diary.diary_name, "hello", "Diary name has changed to\
        hello")

    def test_date_added(self):
        # Tests that the date_added is equal to the given date
        self.assertEqual(self.diary.date_created,
                         "Tue, 25 Sep 2018 23:53:50 GMT")

    def test_class_instance(self):
        # Tests that the defined object is an instance of a class
        self.assertIsInstance(self.diary, Diary)
