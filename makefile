linux: linux-build run

mac: mac-build run

windows: windows-build run

linux-build:
    export FLASK_APP=app.py
    export FLASK_DEBUG=1

mac-build:
    export FLASK_APP=app.py
    export FLASK_DEBUG=1

windows-build:
    set FLASK_APP=app.py
    set FLASK_DEBUG=1

run:
	flask run
