#This script autoates the creation of new projects and automattically creates a new private repository in GitHub
#create GitHub repository
import os
import sys
import requests

# Constants
GITHUB_USERNAME = 'MathiasJoensson'
GITHUB_TOKEN = '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'
MY_PROJECTS_PATH = "C:\\Users\\User\\bioinformatics\\MyProjects"

# Check if project name is provided
if len(sys.argv) < 2:
    print("Please provide project name")
    sys.exit(1)

# Get project name from command line
project_name = sys.argv[1]

# Create project folder in MyProjects
project_path = os.path.join(MY_PROJECTS_PATH, project_name)
os.makedirs(project_path)
print(f"Created project folder {project_path}")

#Navigate to projectfolder
os.chdir(project_path)

#Initialize git repository
os.system("git init")
print("Initialized git repository")

#Create GitHub repository using API
headers = {"Authorization": f"token {GITHUB_TOKEN}"}
data = {"name": project_name, "private": True}
response = requests.post("https://api.github.com/user/repos", json=data, headers=headers)
if response.status_code == 201:
    print("Created GitHub repository")
else:
    print("Failed to create GitHub repository: {response.json()['message']}")
    sys.exit(1)

#Get GitHub repository URL
repo_url = response.json()["clone_url"]

#Add GitHub repository as remote
os.system(f"git remote add origin {repo_url}")
print("Added GitHub repository as remote")

#Create README.md
with open("README.md", "w") as f:
    f.write(f"# {project_name}\n\nThis is a README file for {project_name}.\n")
print("Created README.md")

#Add, commit and push README.md
os.system("git add README.md")
os.system('git commit -m "Initial commit" ')
print("Added and committed README.md")

#Push README.md to GitHub
os.system("git push -u origin main")
print("Pushed README.md to GitHub")

#Open project folder in VS Code
os.system("code .")
