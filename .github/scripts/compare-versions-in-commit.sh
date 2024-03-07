#!/bin/bash

# Get the version number of the current working directory
CURRENT_VERSION_TOML=$(grep -E '^\s*version\s*=\s*"[0-9]+\.[0-9]+\.[0-9]+"' pyproject.toml | awk -F '"' '{print $2}')
CURRENT_VERSION_INIT=$(grep -E '^\s*__version__\s*=\s*"[0-9]+\.[0-9]+\.[0-9]+"' ./visualgo/__init__.py | awk -F '"' '{print $2}')

# Compare the version numbers
if [ "$CURRENT_VERSION_TOML" != "$CURRENT_VERSION_INIT" ]; then
    echo "ERROR : version mismatch in pyproject.toml and visualgo/__init__.py"
    echo "Version in pyproject.toml: $CURRENT_VERSION_TOML"
    echo "Version in visualgo/__init__.py: $CURRENT_VERSION_INIT"
    exit 1
fi
echo "SUCCESS : version match in pyproject.toml and visualgo/__init__.py"
echo "Version in pyproject.toml: $CURRENT_VERSION_TOML"
echo "Version in visualgo/__init__.py: $CURRENT_VERSION_INIT"
exit 0
