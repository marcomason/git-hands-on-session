from pathlib import Path
from git import Repo
import hashlib


GREEN = '\033[92m'
RED = '\033[91m'
ENDCOLOR = '\033[0m'


repo = Repo(Path(".").resolve())

number_of_branches = len(repo.branches)
number_of_commits = len(list(repo.iter_commits()))
repository_status = hashlib.md5(f"{number_of_branches}-{number_of_commits}".encode()).hexdigest()

username = input("Insert the username: ").strip("\n")
expected_result = hashlib.md5(f"{repository_status}-{username}".encode()).hexdigest()
given_result = input("Insert the result from the user: ").strip("\n")

if given_result == expected_result:
    print(f"{GREEN}Good Job!{ENDCOLOR} - {username} has correct repository status.")
else:
    print(f"{RED}Oh No!{ENDCOLOR} - {username} has wrong repository status.")
