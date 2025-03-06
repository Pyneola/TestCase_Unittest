class StubDatabase:
    def get_user(self, user_id):
        return {"id": user_id, "name": f"StubUser{user_id}"}
