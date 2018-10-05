class User:
    """The User is the person who interacts with the application """
    def __init__(self, user_id, user_name, email, password):
        self.user_id = user_id
        self.user_name = user_name
        self.email = email
        self.password = password

    def get_dict(self):
        return {
            'user_id': self.user_id,
            'user_name': self.user_name,
            'email': self.email,
            'password': self.password
        }


class Diary:
    """The Diary is where the user makes and views entries"""
    def __init__(self, diary_id, diary_name, date_created):
        self.diary_id = diary_id
        self.diary_name = diary_name
        self.date_created = date_created

    def serialize(self):
        return {
            'diary_id': self.diary_id,
            'diary_name': self.diary_name,
            'date_created': self.date_created
            }


class Entry:
    """Defines entries made by a user"""
    def __init__(self, entry_id, date_created, entry_text):
        self.entry_id = entry_id
        self.date_created = date_created
        self.entry_text = entry_text

    def toJSON(self):
        return {
            'entry_id': self.entry_id,
            'date_created': self.date_created,
            'entry_text': self.entry_text,
        }
