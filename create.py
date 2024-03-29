#!<path-to-python3-installation>

# Set path to Python 3 installation above
# Put username and password (or access token) 
# in .config folder located in the same directory 
# as the create.py script Add directory to PATH so 
# create.py is executable from anywhere

# Usage: create.py <project_name>



# imports
import os
import subprocess
from github import Github
import sys
sys.path.append('./.config/')
from git_config import username
from git_config import password

# error handling
print('Not enough aguments') if not (len(sys.argv) == 2) else print('Creating {} repository'.format(sys.argv[1]))

# grab repository name from stdin
repo_name = sys.argv[1]
g = Github(username, password)

# set path and url variables // change directory to new proj
path = '/Users/{}/Documents/dev/proj/{}'.format(os.environ.get('USER'), repo_name)
os.mkdir(path)
os.chdir(path)

# touch README and populate with repo name
readme = open('README.md', 'w')
readme.write('# {}'.format(repo_name.capitalize()))
readme.close()

# init git
subprocess.run(['git', 'init'])

# github request
g.get_user().create_repo(name=repo_name, private=True)

# git add origin and push
url = 'https://github.com/{}/{}.git'.format(username, repo_name)
subprocess.run(['git', 'remote', 'add', 'origin', '{}'.format(url)])
subprocess.run(['git', 'add', '*'])
subprocess.run(['git', 'commit', '-m', 'init'])
subprocess.run(['git', 'push', 'origin', 'master'])
