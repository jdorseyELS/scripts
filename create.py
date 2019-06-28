#!/Users/ma-dorseyj/homebrew/miniconda3/bin/python3

## imports
import os
import subprocess
from github import Github
from sys import argv

## grab repository name from stdin
repo_name = argv[1]
user = argv[2]

g = Github("4a2d678cf68d886e8d5fbb1350d643ba4d4f75cf")
print('Not enough aguments') if not (len(argv) == 2) else print('Creating {} repository'.format(repo_name))

## set path and url variables // change directory to new proj
path = '/Users/{}/Documents/dev/proj/{}'.format(os.environ.get('USER'), repo_name)
os.mkdir(path)
os.chdir(path)

# ## touch README and populate with repo name
readme = open('README.md', 'w')
readme.write('# {}'.format(repo_name.capitalize()))
readme.close()

## init git
subprocess.run(['git', 'init'])

## github request
g.get_user().create_repo(name=repo_name, private=True)

## git add origin and push
url = 'https://github.com/{}/{}.git'.format(user, repo_name)
subprocess.run(['git', 'remote', 'add', 'origin', '{}'.format(url)])
subprocess.run(['git', 'add', '*'])
subprocess.run(['git', 'commit', '-m', 'init'])
subprocess.run(['git', 'push', 'origin', 'master'])



