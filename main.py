import subprocess

# Define the repository path
repository_path = '/Users/jacobhill/Desktop/Avian Identifier'

# Define the file path and the line of code to add
file_path = '/Users/jacobhill/Desktop/Avian Identifier/attempt/frontend/avian_frontend/src/pages/LogBird.jsx'
new_line = 'console.log("Hello, Tenz!")'

# Change directory to the repository path
subprocess.call(['cd', repository_path])

# Add the new line of code to the file
subprocess.call(['echo', new_line, '>>', file_path])

# Commit the changes
subprocess.call(['git', 'add', file_path])
subprocess.call(['git', 'commit', '-m', 'Added new line of code'])

# Push the changes to GitHub
subprocess.call(['git', 'push', 'origin', 'master'])