import subprocess
import sys

def cherryPickToBranch(branch, commitHash):
    try:
        # Create and switch to new branch from main
        subprocess.run(['git', 'checkout', '-b', branch, 'main'])
        print(f'Branch "{branch}" successfully created from main.')

        # Cherry-pick the commit
        subprocess.run(['git', 'cherry-pick', commitHash])
        print(f'Successfully cherry-picked commit {commitHash} into {branch}\n')

    except subprocess.CalledProcessError as e:
        print(f"Error in branch '{branch}': {e}")
        print("You may need to resolve conflicts manually:")
        print("git status\n   git add <conflicted-files>\n   git cherry-pick --continue\n")
        subprocess.run(['git', 'cherry-pick', '--abort'], check=False)

def cherryPick(commitHash, branches):
    for branch in branches:
        cherryPickToBranch(branch, commitHash)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python cherryPick.py <commit-hash> <branch1> [<branch2> ...]")
        sys.exit(1)

    commitHash = sys.argv[1]
    branches = sys.argv[2:]
    cherryPick(commitHash, branches)
