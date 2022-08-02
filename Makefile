format:
	isort kedro_light
	black kedro_light

install:
	pip install -e .[dev]

verify:
	isort --check --diff kedro_light
	black --check --diff kedro_light
	flake8 kedro_light

