documentation:
	pdoc --html --force --output-dir docs kedro_light
	mv docs/kedro_light/* docs
	rmdir docs/kedro_light

format:
	isort kedro_light
	black kedro_light

install:
	pip install -e .[dev]

link_readme:
	ln -sr README.md kedro_light/README.md

verify:
	isort --check --diff kedro_light
	black --check --diff kedro_light
	flake8 kedro_light
	$(MAKE) documentation

