<h1 align="center">Python CI/CD Demo Setup</h1>
<h2 align="center">A demonstration Python CI/CD Configuration</h2>
<p align="center">
<a href="https://github.com/Matthew-Redrup/python-cicd-demo/actions"><img alt="Actions Status" src="https://github.com/Matthew-Redrup/python-cicd-demo/actions/workflows/test.yml/badge.svg"></a>
<a href="https://codecov.io/gh/Matthew-Redrup/python-cicd-demo" > 
<img src="https://codecov.io/gh/Matthew-Redrup/python-cicd-demo/graph/badge.svg?token=4X9WNUJ49K"/> 
</a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>


This is a demonstration repostitory for a Python project with a CI/CD configuration. The main branch uses Poetry as the build tool. Check other branches for alternate build tools. When starting a new project you should be able to copy the configuration files from this repository and get started with CI/CD straight away.

The source files do not contain any useful code and are only used to demonstrate the CI/CD configuration with a simple unit test.


# Installation and Usage

## Installation

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
