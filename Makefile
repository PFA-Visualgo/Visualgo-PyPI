# Makefile

# Default target
all: venv install static-analysis build test

# Set the appropriate Python executable based on the platform
PYTHON := $(shell command -v python3 2> /dev/null || command -v python)
VENV := venv

RESET = \033[0m
BOLD = \033[1m
GREEN = \033[32m
RED = \033[31m

# Target to create the virtual environment
venv:
	@echo "$(BOLD)$(GREEN)>> Setting up virtual environment <<$(RESET)"
	@$(PYTHON) -m venv $(VENV)

# Install dependencies from requirements.txt
install: requirements.txt
	@echo "$(BOLD)$(GREEN)>> Installing dependencies <<$(RESET)"
	@. venv/bin/activate; pip install install -Ur requirements.txt

# Run the main application
static-analysis:
	@echo "$(BOLD)$(GREEN)>>Running static analysis <<$(RESET)"

	@echo "should use something like flake8"

build:
	@echo "$(BOLD)$(GREEN)>>Building the application <<$(RESET)"

	@. venv/bin/activate; python -m pip  install --upgrade pip
	@. venv/bin/activate; pip install build
	@. venv/bin/activate; python -m build


test:
	@echo "$(BOLD)$(GREEN)>>Running tests <<$(RESET)"

	@. venv/bin/activate; python -m unittest discover -s tests -v


# Clean up the project
clean:
	@echo "$(BOLD)$(GREEN)>>Cleaning up <<$(RESET)"
	@rm -rf $(VENV)
	@echo "$(BOLD)$(GREEN)Project cleaned correctly.$(RESET)"

# Define phony targets
.PHONY: all venv install run clean
