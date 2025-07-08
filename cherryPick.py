import subprocess, sys, ast
def cherryPickToBranch(branch, commitHash, baseBranch):
    print(branch, commitHash, baseBranch, end='\n')
    try:
        # Create and switch to new branch from main
        subprocess.run(['git', 'checkout', '-b', branch, baseBranch])
        print(f'Branch "{branch}" successfully created from main.')

        # Cherry-pick the commit
        subprocess.run(['git', 'cherry-pick', commitHash])
        print(f'Successfully cherry-picked commit {commitHash} into {branch}\n')
        print(branch, baseBranch)

    except subprocess.CalledProcessError as e:
        print(f"Error in branch '{branch}': {e}")
        print("You may need to resolve conflicts manually:")
        print("git status\n   git add <conflicted-files>\n   git cherry-pick --continue\n")
        subprocess.run(['git', 'cherry-pick', '--abort'], check=False)

def cherryPick(commitHash, branches, baseBranches):
    for index in range(len(branches)):
        cherryPickToBranch(branches[index], commitHash, baseBranches[index])

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python cherryPick.py <commit-hash> <branch1> [<branch2> ...]")
        sys.exit(1)

    commitHash = sys.argv[1]
    branches = ast.literal_eval(sys.argv[2])
    baseBranches = ast.literal_eval(sys.argv[3])
    cherryPick(commitHash, branches, baseBranches)
