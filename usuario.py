class User:
    def __init__(self, user_name, user_email, user_phone):
        self.user_name = user_name
        self.user_email = user_email
        self.user_phone = user_phone

    def toDBCollection(self):
        return {
            'user_name': self.user_name,
            'user_email': self.user_email,
            'user_phone': self.user_phone
        }
