#!/bin/bash

# Check if the GitHub CLI is installed
if ! command -v gh &> /dev/null; then
    echo "GitHub CLI (gh) is not installed. Please install it from https://cli.github.com/."
    exit 1
fi

# Check if the current directory is empty
if [ -z "$(ls -A)" ]; then
    echo "The current directory is empty. Please add files to the directory before running the script."
    exit 1
fi

# Initialize a new Git repository
git init

# Add all files in the current directory to the repository
git add .

# Commit the changes
git commit -m "Initial commit"

# Create a new GitHub repository using the GitHub CLI
echo -n "Enter the name of the GitHub repository: "
read -r repo_name

# Validate the repository name
if [[ ! "$repo_name" =~ ^[a-zA-Z0-9_-]+$ ]]; then
    echo "Invalid repository name. Please use only alphanumeric characters, hyphens, or underscores."
    exit 1
fi

gh repo create "$repo_name" --public

# Set the remote origin URL for the repository
gh_repo_url=$(gh repo view "$repo_name" --json ssh_url -q ".ssh_url")
git remote add origin "$gh_repo_url"

# Push the local repository to the GitHub repository
git push -u origin master

echo "Local repository has been initialized, committed, and pushed to the GitHub 
