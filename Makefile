format:
	python -m black --config pyproject.toml .

lint:
	python -m flake8 --config lint.cfg
	python -m black  --config pyproject.toml --check .

install:
	pip install --editable .
