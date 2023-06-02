import subprocess

# Define the repository path
repository_path = '/Users/jacobhill/Desktop/new_line'

# Define the file path and the line of code to add
file_path = '/Users/jacobhill/Desktop/new_line/print.py'
new_line = 'print("Hello, World!")'

# Change directory to the repository path
subprocess.call(['cd', repository_path])

# Add the new line of code to the file
with open(file_path, 'a') as file:
    file.write('\n' + new_line)

# Commit the changes
subprocess.call(['git', 'add', file_path])
subprocess.call(['git', 'commit', '-m', 'Added new line of code'])

# Push the changes to GitHub
subprocess.call(['git', 'push', 'origin', 'master'])