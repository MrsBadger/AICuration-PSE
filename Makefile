#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
PROJECT_NAME = app

install:
	pipenv install
	pipenv run pip install -e .

test:
	pytest src -o log_cli=true --log-cli-level=INFO -p no:warnings

build:
	docker build -t $(PROJECT_NAME) .

run:
	docker run -it \
		--name $(PROJECT_NAME) $(PROJECT_NAME)

build_run: build run
