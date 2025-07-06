import subprocess

def cherryPick(branch, commitHash):
    try:
        subprocess.run(['git', 'checkout', '-b', branch])
        print(f'Branch {branch} sucessfully created!')
        subprocess.run(['git', 'cherry-pick', commitHash])
        print(f"Successfully cherry-picked commit {commitHash}")
        
    except subprocess.CalledProcessError as e:
        print(f"Error during cherry-pick: {e}")
        
        
cherryPick('feature', '8e2e3b13318f0968e3462778444f836922e51efe' )