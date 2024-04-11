# AICuration-PSE
Test task for the position of PS Engineer

---

##### Project structure:
    /app
        /core
            app.py
            utils.py
            settings.py
        main.py
    /tests
    Dockerfile
    Makefile
    Pipfile
    Pipfile.lock


##### Getting started

1. Add .env file to the root of the project
2. Fill in the variables in the .env file. You can use the .env.example file as an example


##### How to run the project using docker
1. make run
2. Find the results in the http://0.0.0.0:8000/analysis


##### How to run the project using pipenv
1. pipenv install
2. pipenv run python app/main.py
3. Find the results in the http://0.0.0.0:8000/analysis
