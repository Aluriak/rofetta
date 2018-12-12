

all:
	python -m rofetta

t: tests
tests:
	pytest test/ rofetta -vv --doctest-module --ignore=venv

.PHONY: tests t all install_deps


install_deps:
	python -c "import configparser; c = configparser.ConfigParser(); c.read('setup.cfg'); print(c['options']['install_requires'])" | xargs pip install -U

release: fullrelease
fullrelease:
	fullrelease
