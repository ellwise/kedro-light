.PHONY: build
build:
	python -m build --outdir _dist

.PHONY: compile
compile:
	pip-compile --output-file requirements.txt --extra dev pyproject.toml

.PHONY: deploy
deploy:
	mkdocs gh-deploy --force

.PHONY: distribute
distribute: build
	twine upload _dist/*

.PHONY: format
format:
	isort .
	black .

.PHONY: install
install:
	pip install -r requirements.txt
	pip install -e .

.PHONY: serve
serve:
	mkdocs serve

.PHONY: verify
verify:
	isort --check --diff .
	black --check --diff .
	ruff check .
