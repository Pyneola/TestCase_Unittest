class Database:
    def get_user(self, user_id):
        raise NotImplementedError("This method should be mocked!")


def fetch_user_name(db, user_id):
    user = db.get_user(user_id)
    return user.get("name", "Unknown")
