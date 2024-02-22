# Makefile

# Default target
all: install static-analysis build tests

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
	@echo "export PYTHONPATH=$$PWD/src:\$$PYTHONPATH" >> $(VENV)/bin/activate

# Install dependencies from requirements.txt
install: venv requirements.txt
	@echo "$(BOLD)$(GREEN)>> Installing dependencies <<$(RESET)"
	@. venv/bin/activate; pip install -Ur requirements.txt

# Run the main application
static-analysis: install
	@echo "$(BOLD)$(GREEN)>>Running static analysis <<$(RESET)"
	@echo "should use something like flake8"

build: install
	@echo "$(BOLD)$(GREEN)>>Building the application <<$(RESET)"
	@. venv/bin/activate; python -m pip  install --upgrade pip
	@. venv/bin/activate; pip install build
	@. venv/bin/activate; python -m build

freeze:
	@echo "$(BOLD)$(GREEN)>>Freezing the dependencies <<$(RESET)"
	@echo "$(BOLD)$(GREEN) Make sure to run the tests with the virtual environment activated.$(RESET)"
	@pip freeze > requirements.txt

tests: install
	@echo "$(BOLD)$(GREEN)>>Running tests <<$(RESET)"
	@python -m pytest --cov=src/visualgo --cov-report=html --cov-report=term-missing tests/
	@echo "$(BOLD)$(GREEN)>> Coverage HTML report can be found in htmlcov/index.html <<$(RESET)"


# Clean up the project
clean:
	@echo "$(BOLD)$(GREEN)>>Cleaning up <<$(RESET)"
	@rm -rf $(VENV) dist htmlcov
	@echo "$(BOLD)$(GREEN)Project cleaned correctly.$(RESET)"

# Define phony targets
.PHONY: all venv install run clean tests freeze
