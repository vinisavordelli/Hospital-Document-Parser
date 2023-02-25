start:
		python backend/src/main.py

test:
		python -m pytest backend/tests

install:
		pip install -r requirements.txt

run:
		python backend/src/start.py