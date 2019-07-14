init:
	@pip3 install -r requirements.txt

run:
	@python3 app/main.py

run-god:
	@python3 app/main.py True

tests:
	@nosetests --rednose test

help:
	@echo There are following possible commands:
	@echo 	make init: installs requirements
	@echo 	make test: runs tests
	@echo 	make run: runs the game with a random configuration
	@echo 	make run-god: runs the game in god mode.
	@echo   ______________________________________________
	@echo   Use the following keys to play god:
	@echo   MouseButton 1 to create
	@echo	MouseButton 2 to destroy
	@echo	Space to destroy everything
	@echo	ENTER to start
