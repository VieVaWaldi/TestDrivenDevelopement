init:
	@pip3 install -r requirements.txt

run:
	@python3 app/main.py

tests:
	@nosetests --rednose test

help:
	@echo There are following possible commands:
	@echo 	make init: installs requirements
	@echo 	make run: runs the game
	@echo 	make test: runs tests
