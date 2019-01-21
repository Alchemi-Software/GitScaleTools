import subprocess,os

class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)

folders = os.listdir()
dont = ["ignore","sync.py"]
for me in dont:
    if me in folders:
        folders.remove(me)

for folder in folders:
    # enter the directory like this:
    with cd(folder):
        os.system("git pull")
        os.system("git add *")
        os.system("git commit -m 'Auto'")
        os.system("git push")
    os.system("rmdir /q /s " + folder)
