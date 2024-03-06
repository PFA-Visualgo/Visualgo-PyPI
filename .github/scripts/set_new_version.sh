#!/bin/bash

# Get the current date in the Paris timezone
CURRENT_DATE_PARIS=$(TZ="Europe/Paris" date +"%Y.%-m.%-d")

# Get the version number of the current working directory
CURRENT_VERSION=$(git show origin/master:pyproject.toml | grep -E '^\s*version\s*=\s*"[0-9]+\.[0-9]+\.[0-9]+"' | awk -F '"' '{print $2}')
# echo "Version in the current commit: $CURRENT_VERSION"

if [ "$CURRENT_VERSION" == "$CURRENT_DATE_PARIS" ]; then
    # Get the day version release
    CURRENT_VERSION=$(grep -Po 'version\s*=\s*"\d+\.\d+\.\d+\-rev\K\d+' pyproject.toml)
    # add 1 to the version number
    NEW_VERSION_NUMBER=$(expr $CURRENT_VERSION + 1)
    NEW_VERSION="$CURRENT_DATE_PARIS-rev$NEW_VERSION_NUMBER"

else
    NEW_VERSION="$CURRENT_DATE_PARIS"
fi

echo "New version: $NEW_VERSION"

# Update the version number in the pyproject.toml file and src/visualgo/__init__.py file

# Update the version number in the pyproject.toml file
sed -i "s/version = \".*\"/version = \"$NEW_VERSION\"/" pyproject.toml

# Update the version number in the src/visualgo/__init__.py file
sed -i "s/__version__ = \".*\"/__version__ = \"$NEW_VERSION\"/" src/visualgo/__init__.py
