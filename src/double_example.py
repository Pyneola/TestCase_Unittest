class Database:
    def get_user(self, user_id):
        raise NotImplementedError("This method should be mocked!")


def fetch_user_name(db, user_id):
    try:
        user = db.get_user(user_id)
        if user is None or not user.get("name"):
            return "Unknown"
        return user["name"]
    except Exception:
        return "Unknown"
