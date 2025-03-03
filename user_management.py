# user_management.py

import json
import os

class User:
    def __init__(self, username, password=None):
        self.username = username
        self.password = password
        self.saved_stories = []
        self.preferences = {}
        self.role = 'user'  # Default role

    @staticmethod
    def load_users_from_json(file_path):
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                data = json.load(file)
                return data.get("users", [])
        return []

    @staticmethod
    def save_users_to_json(file_path, users):
        with open(file_path, 'w') as file:
            json.dump({"users": users}, file)

    def save_story(self, story):        
        print(f"Story '{story}' saved by {self.username}.")  # Log activity
        self.saved_stories.append(story)

    def set_preference(self, key, value):
        self.preferences[key] = value
        print(f"Preference '{key}' set to '{value}' for {self.username}.")  # Log activity

    def get_preference(self, key):
        print(f"Retrieved preference '{key}' for {self.username}.")  # Log activity
        return self.preferences.get(key, None)

    def delete_story(self, story):        
        if story in self.saved_stories:
            self.saved_stories.remove(story)
            print(f"Story '{story}' deleted by {self.username}.")  # Log activity
        else:
            print(f"Story '{story}' not found for {self.username}.")  # Log activity

    def edit_story(self, old_story, new_story):        
        if old_story in self.saved_stories:
            index = self.saved_stories.index(old_story)
            self.saved_stories[index] = new_story
            print(f"Story '{old_story}' edited to '{new_story}' by {self.username}.")  # Log activity
        else:
            print(f"Story '{old_story}' not found for {self.username}.")  # Log activity

def get_user(username, password=None):
    # Here you can add logic to validate the user credentials
    return User(username, password)



    def save_story(self, story):        
        print(f"Story '{story}' saved by {self.username}.")  # Log activity
        self.saved_stories.append(story)

    def set_preference(self, key, value):
        self.preferences[key] = value
        print(f"Preference '{key}' set to '{value}' for {self.username}.")  # Log activity

    def get_preference(self, key):
        print(f"Retrieved preference '{key}' for {self.username}.")  # Log activity
        return self.preferences.get(key, None)

    def delete_story(self, story):        
        if story in self.saved_stories:
            self.saved_stories.remove(story)
            print(f"Story '{story}' deleted by {self.username}.")  # Log activity
        else:
            print(f"Story '{story}' not found for {self.username}.")  # Log activity

    def edit_story(self, old_story, new_story):        
        if old_story in self.saved_stories:
            index = self.saved_stories.index(old_story)
            self.saved_stories[index] = new_story
            print(f"Story '{old_story}' edited to '{new_story}' by {self.username}.")  # Log activity
        else:
            print(f"Story '{old_story}' not found for {self.username}.")  # Log activity

def get_user(username, password=None):
    # Here you can add logic to validate the user credentials
    return User(username, password)
