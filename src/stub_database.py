class StubDatabase:
    def get_user(self, user_id):
        if not isinstance(user_id, int):
            raise TypeError("user_id must be an integer")
        return {"id": user_id, "name": f"StubUser{user_id}"}
