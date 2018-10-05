import unittest
from api.models import Entry


class TestEntry(unittest.TestCase):
    def setUp(self):
        self.entry = Entry(1, "Tue, 25 Sep 2018 23:53:50 GMT", "Hello am me!")

    def test_entry_id(self):
        # Tests that the entry_id is equal to the given entry_id
        self.assertEqual(self.entry.entry_id, 1, "entry_id must be 1")
        self.entry.entry_id = 2
        self.assertEqual(self.entry.entry_id, 2, "entry_id is now 2")

    def test_date_added(self):
        # Tests that the date_added is equal to the given date
        self.assertEqual(self.entry.date_created,
                         "Tue, 25 Sep 2018 23:53:50 GMT")

    def test_entry_text(self):
        # Tests that the entry text is equal to the given content
        self.assertEqual(self.entry.entry_text, "Hello am me!")
        self.entry.entry_text = "hey"
        self.assertEqual(self.entry.entry_text, "hey", "Entry text has changed to\
        hey")

    def test_class_instance(self):
        # Tests that the defined object is an instance of a class
        self.assertIsInstance(self.entry, Entry)
