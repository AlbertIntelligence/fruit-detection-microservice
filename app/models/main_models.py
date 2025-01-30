# app/models.py
class User:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

    # Example method to simulate retrieving a user by id (in real use, you might interact with a database)
    @classmethod
    def get_user_by_id(cls, user_id):
        # This is just a placeholder logic. You would replace this with a real DB query.
        return cls(user_id, "John Doe", "john@example.com")
