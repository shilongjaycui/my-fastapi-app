install:
	pip install --upgrade pip
	pip install pre-commit flake8 flake8-docstrings Flake8-pyproject radon pylint mypy black isort
	pre-commit sample-config > .pre-commit-config.yaml
	pre-commit autoupdate
	pre-commit install

synth-project:
	npx projen

lint:
	pre-commit run --all-files

unit-test:
	pytest