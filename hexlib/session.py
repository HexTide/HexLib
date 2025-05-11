import os
import json

class SessionManager:
    def __init__(self, session_dir="sessions"):
        self.session_dir = session_dir
        os.makedirs(self.session_dir, exist_ok=True)

    def get_session_path(self, user_id):
        return os.path.join(self.session_dir, f"{user_id}.json")

    def load(self, user_id):
        path = self.get_session_path(user_id)
        if not os.path.exists(path):
            return {}
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)

    def save(self, user_id, data):
        path = self.get_session_path(user_id)
        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2)
