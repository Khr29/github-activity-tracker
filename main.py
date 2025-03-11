from github_api import get_github_activity
from utils import display_activity

def main():
    username = input("Enter GitHub username: ")
    events = get_github_activity(username)
    display_activity(events)

if __name__ == "__main__":
    main()