# Default command will read contents of the makefile
default:
	@cat makefile


PHONY: newStart openApp openAppDev cleanUp
# Command will create a virtual env (remove any existing), open the application, and start the server
newStart:
	@pipenv install
	@pipenv shell
	@open -a "Google Chrome" http://127.0.0.1:8000/
	@python backend/main.py


# Command will open the application and start the server
openApp:
	@open -a "Google Chrome" http://127.0.0.1:8000/
	@python backend/main.py


# Command will open the application docs page
openAppDev:
	@open -a "Google Chrome" http://127.0.0.1:8000/docs
	@python backend/main.py


# Command will delete any virtual env
cleanUp:
	@bash deactivate
	@pipenv --rm