#!/bin/bash

# Get the version number of the last commit on the master branch
MASTER_VERSION=$(git show origin/master:pyproject.toml | grep -E '^\s*version\s*=\s*"[0-9]+\.[0-9]+\.[0-9]+"' | awk -F '"' '{print $2}')
# TODO use correct master path


# Get the version number of the current working directory
CURRENT_VERSION=$(grep -E '^\s*version\s*=\s*"[0-9]+\.[0-9]+\.[0-9]+"' pyproject.toml | awk -F '"' '{print $2}')

# Compare the version numbers
if [ "$MASTER_VERSION" == "$CURRENT_VERSION" ]; then
    echo "ERROR : matched master version"
    echo "Version in the current commit: $CURRENT_VERSION"
    echo "Version on master: $MASTER_VERSION"
    exit 1
else
    echo "SUCESS : not matched master version"
    echo "Version in the current commit: $CURRENT_VERSION"
    echo "Version on master: $MASTER_VERSION"
    exit 0
fi
