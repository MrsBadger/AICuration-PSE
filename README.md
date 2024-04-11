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
    Dockerfile
    Makefile
    Pipfile
    Pipfile.lock


##### Getting started
0. To work with the project, if you have no programming experience, I advise you to download [VSCode](https://code.visualstudio.com/download)
1. Сlone the repository locally on your computer. Detailed instructions can be found in the official Github documentation: [link](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
2. Create a .env file in the project root (the root of the repository means your local folder, which contains all files and folders cloned from the remote repository)
3. Fill in the variables in the .env file. You can use the .env.example file as an example (by default, the required endpoints are already indicated there)


##### How to run the project using docker
1. Get docker: [documentation link](https://docs.docker.com/get-docker/)
2. Find [terminal](https://code.visualstudio.com/docs/terminal/basics) in your VSCode
3. Copy and paste the following command into the terminal, then press enter: `make run`
4. You can find the results from the link below, just open it in any browser: http://0.0.0.0:8000/analysis


##### How to run the project using pipenv (only for advanced users! ❌)
1. `pipenv install`
2. `pipenv run python app/main.py`
3. You can find the results from the link below, just open it in any browser: http://0.0.0.0:8000/analysis
