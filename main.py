import subprocess
import os

# Define the repository path
repository_path = '/Users/jacobhill/Desktop/new_line'

# Define the file path and the line of code to add
file_path = '/Users/jacobhill/Desktop/new_line/print.py'
new_line = 'print("Hello, There!")'

# Change directory to the repository path
subprocess.call(['cd', repository_path], stdout=open(os.devnull, "wb"))

# Add the new line of code to the file
subprocess.call(['echo', new_line, '>>', file_path], stdout=open(os.devnull, "wb"))

# Commit the changes
subprocess.call(['git', 'add', file_path], stdout=open(os.devnull, "wb"))
subprocess.call(['git', 'commit', '-m', 'Added new line of code'], stdout=open(os.devnull, "wb"))

# Push the changes to GitHub
subprocess.call(['git', 'push', 'origin', 'main'], stdout=open(os.devnull, "wb"))