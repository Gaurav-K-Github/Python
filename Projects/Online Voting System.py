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
        
    def login_user(self, username, password):
        if username in self.users and self.users[username] == password:
            return True
        else:
            return False
            
    def add_candidate(self, candidate):
        self.candidates[candidate] = 0
        
    def vote(self, candidate):
        if candidate in self.candidates:
            self.candidates[candidate] += 1
            return True
        else:
            print("Invalid candidate.")
            return False
            
    def display_candidates(self):
        print("Candidates:")
        for candidate in self.candidates:
            print(candidate)

    def display_candidates(self):
        print("Candidates:")
        for candidate in self.candidates:
            print(candidate)

    def display_results(self):
        print("Voting Results:")
        for candidate, votes in self.candidates.items():
            print(f"{candidate}: {votes} votes")

def main():
    voting_system = VotingSystem()

    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Add Candidate")
        print("4. Vote")
        print("5. Display Candidates")
        print("6. Display Results")
        print("7. Exit")

        choice = input("Enter your choice: ")


