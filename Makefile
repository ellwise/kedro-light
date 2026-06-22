.PHONY: build
build:
	uv build --out-dir _dist

.PHONY: docs
docs:
	uv run mkdocs serve

.PHONY: docs-deploy
docs-deploy:
	uv run mkdocs gh-deploy --force

.PHONY: format
format:
	uv run ruff format .
	uv run ruff check --fix .

.PHONY: install
install:
	uv sync

.PHONY: lint
lint:
	uv run ruff format --check --diff .
	uv run ruff check .

.PHONY: publish
publish: build
	uv publish
