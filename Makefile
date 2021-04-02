install:
	python3 -m pip install --user dist/*.whl

uninstall:
	python3 -m pip uninstall hexlet-code

lint:
	poetry run flake8 gendiff

test:
	pytest tests/test.py