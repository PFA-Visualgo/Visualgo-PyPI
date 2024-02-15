#!/bin/bash

# Get the version number of the current working directory
CURRENT_VERSION=$(grep -E '^\s*version\s*=\s*"[0-9]+\.[0-9]+\.[0-9]+"' pyproject.toml | awk -F '"' '{print $2}')

# Get the current date in the Paris timezone
CURRENT_DATE_PARIS=$(TZ="Europe/Paris" date +"%Y.%-m.%-d")

# Compare the version number with the current date in Paris timezone
if [ "$CURRENT_VERSION" == "$CURRENT_DATE_PARIS" ]; then
    echo "SUCESS : matched paris date"
    echo "Version in the current commit: $CURRENT_VERSION"
    echo "Current date in Paris timezone: $CURRENT_DATE_PARIS"
    exit 0
else
    echo "ERROR : not match paris date"
    echo "Version in the current commit: $CURRENT_VERSION"
    echo "Current date in Paris timezone: $CURRENT_DATE_PARIS"
    exit 1
fi
