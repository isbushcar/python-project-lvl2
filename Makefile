install:
	python3 -m pip install --user dist/*.whl

uninstall:
	python3 -m pip uninstall hexlet-code

lint:
	poetry run flake8 gendiff/

test:
	poetry run pytest -vv tests/test.py

coverage:
	poetry run pytest --cov=gendiff tests/test.py --cov-report xml