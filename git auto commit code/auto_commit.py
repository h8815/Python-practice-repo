import os
import datetime
from git import Repo
import auto_password

# Replace this with the path to your local repo
REPO_PATH = "C:\\Users\\Himanshu\\Documents\\Auto-password_shell-script"

def auto_commit():
    # Initialize repo
    repo = Repo(REPO_PATH)
    file_path = os.path.join(REPO_PATH, "password_change_sample.log")

    # Generate password log from auto_password
    auto_password_output = auto_password.main()

    # Append to log file with UTF-8 encoding
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(f"{auto_password_output}")

    # Stage all changes
    repo.git.add(all=True)

    # Commit changes
    commit_message = f"Log update: {datetime.datetime.now().strftime('%Y-%m-%d 00:00:01')}"
    repo.index.commit(commit_message)

    # Safely pull first (to prevent push error), then push
    origin = repo.remote(name='origin')
    try:
        origin.pull(rebase=True)
        origin.push()
        print("✅ Committed and pushed successfully!")
    except Exception as e:
        print(f"❌ Git push failed: {e}")

if __name__ == "__main__":
    auto_commit()
