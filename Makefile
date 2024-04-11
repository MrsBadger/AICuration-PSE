#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
PROJECT_NAME = app

install:
	pipenv install
	pipenv run pip install -e .

build:
	docker build -t $(PROJECT_NAME) .

run: build
	docker run -it \
		--env-file .env \
		-p 8000:8000 \
		--name $(PROJECT_NAME) $(PROJECT_NAME)
