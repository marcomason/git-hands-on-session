from pathlib import Path
from git import Repo
import hashlib


repo = Repo(Path(".").resolve())

number_of_branches = len(repo.branches)
number_of_commits = len(list(repo.iter_commits()))
username = repo.config_reader().get_value("user", "name")

repository_status = hashlib.md5(f"{number_of_branches}-{number_of_commits}".encode()).hexdigest()
result = hashlib.md5(f"{repository_status}-{username}".encode()).hexdigest()

print(f"Your username is: {username}")
print(f"Your result is: {result}")
