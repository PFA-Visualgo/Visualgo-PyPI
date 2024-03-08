# Makefile

# Default target
all: static-analysis tests

BOLD := $(shell tput bold)
GREEN := $(shell tput setaf 2)
RESET := $(shell tput sgr0)
RED := $(shell tput setaf 1)

export PYTHONPATH := $(PWD)/src:$(PYTHONPATH)

# Check if the virtual environment is activated and not the default Conda environment
check-venv:
	@if [ -n "$$VIRTUAL_ENV" ]; then \
		echo "$(BOLD)$(GREEN)>> Virtual environment is activated (venv) <<$(RESET)"; \
	elif [ -n "$$CONDA_PREFIX" ] && [ "$$CONDA_PREFIX" != "$$(conda info --base)" ]; then \
		echo "$(BOLD)$(GREEN)>> Conda environment is activated and not the default Conda environment <<$(RESET)"; \
	elif [ -n "$$PYENV_VIRTUAL_ENV" ]; then \
		echo "$(BOLD)$(GREEN)>> Virtual environment is activated (pyenv) <<$(RESET)"; \
	elif [ -n "$$PIPENV_ACTIVE" ]; then \
		echo "$(BOLD)$(GREEN)>> Virtual environment is activated (pipenv) <<$(RESET)"; \
	else \
		echo "$(BOLD)$(RED)>> Error: Virtual environment not activated. Please activate your virtual environment of choice. <<$(RESET)"; \
		exit 1; \
	fi

# Install dependencies from requirements.txt
install: check-venv requirements.txt
	@echo "$(BOLD)$(GREEN)>> Installing dependencies <<$(RESET)"
	pip install -r requirements.txt

# Run the main application
static-analysis: install
	@echo "$(BOLD)$(GREEN)>>Running static analysis <<$(RESET)"
	@echo "should use something like flake8"

build: install
	@echo "$(BOLD)$(GREEN)>>Building the application <<$(RESET)"
	python -m pip  install --upgrade pip
	pip install build
	python -m build

build_wheel: install
	@echo "$(BOLD)$(GREEN)>>Building only the wheel of the application <<$(RESET)"
	python -m pip  install --upgrade pip
	pip install build
	python -m build --wheel

freeze:
	@echo "$(BOLD)$(GREEN)>>Freezing the dependencies <<$(RESET)"
	pip freeze > requirements.txt

tests: install
	@echo "$(BOLD)$(GREEN)>>Running tests <<$(RESET)"
	python -m pytest --cov=src/visualgo --cov-report=html --cov-report=term-missing tests/
	@echo "$(BOLD)$(GREEN)>> Coverage HTML report can be found in htmlcov/index.html <<$(RESET)"

tests_outputs: install
	@echo "$(BOLD)$(GREEN)>>Running tests <<$(RESET)"
	python -m pytest -s --cov=src/visualgo --cov-report=html --cov-report=term-missing tests/
	@echo "$(BOLD)$(GREEN)>> Coverage HTML report can be found in htmlcov/index.html <<$(RESET)"


# Clean up the project
clean:
	@echo "$(BOLD)$(GREEN)>>Cleaning up <<$(RESET)"
	rm -rf build dist htmlcov .pytest_cache .coverage
	@echo "$(BOLD)$(GREEN)Project Visualgo-PyPI cleaned correctly.$(RESET)"

# Define phony targets
.PHONY: all check-venv install run clean tests freeze
