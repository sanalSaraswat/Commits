import subprocess
import sys

def cherryPick(branch, commitHash):
    try:
        subprocess.run(['git', 'checkout', '-b', branch, 'main'])
        print(f'Branch {branch} sucessfully created!')
        subprocess.run(['git', 'cherry-pick -m 1 ', commitHash])
        print(f"Successfully cherry-picked commit {commitHash}")
        
    except subprocess.CalledProcessError as e:
        print(f"Error during cherry-pick: {e}")
        
        
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python cherryPick.py <branch> <commit-hash>")
        sys.exit(1)
    branch = sys.argv[1]
    commitHash = sys.argv[2]
    cherryPick(branch, commitHash)