# Python CI/CD Demo Setup
Python project demo repository with a starting CICD config. The main branch uses Poetry as the build tool. Check other branches for alternate build tools.


# Setup and Usage

## Setup

Install using Poetry:
```bash
poetry install
```

## Testing

Run the tests:
```bash
poetry run python -m pytest tests
```

Run code quality checks
```bash
poetry run black .
poetry run isort . --profile black
poetry run flake8 .
poetry run bandit .
poetry run safety check
```
