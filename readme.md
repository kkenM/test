# Test Repo for Learning Github

# Initialize a repository (you only do this once at the start of a project to initalize the project)

git clone <repository link>

# After you've created some code and want to push it to the remote repositry

Create a branch that isn't the main branch (usually you would do this before you make changes it just copies main under a new name)

git branch <new-branch-name>

git checkout <new-branch-name>

Adding your changes

git add .

^ This will add all the files from current working directory (i.e the parent folder of repo)

git commit -m "description of changes"

^ This commits your changes to the local git repository

git push

^ This pushes your changes to the remote GitHub repo

# When you start working for the day ensure you have the latest version of the codebase

git checkout main

^ make sure your fetching the main branch

git fetch

^ fetches the data for the changes in the remote repo.

git pull

^ pulls the changes from the remote repo

# If there is a conflict

You probably made changes in main that conflict with the remote main file. You'll have to put your changes in a new branch and push them.

Refer to the section "After you've created some code and want to push it to the remote repositry"
