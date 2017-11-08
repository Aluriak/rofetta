

all:
	python -m rofetta

t: tests
tests:
	pytest test/

.PHONY: tests t all
