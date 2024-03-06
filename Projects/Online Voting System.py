#PROJECT UNDER DEVELOPMENTAL STAGE

class VotingSystem:
    def __init__(self):
        self.users = {}
        self.candidates = {}
        self.votes = {}

    def register_user(self, username, password):
        if username in self.users:
            print("User already exists. Please choose another username.")
            return False
        self.users[username] = password
        return True
