#!/usr/bin/env sh

PYTHON_EXEC=${PYTHON_EXEC:-"uv run"}
PROJECT_FOLDER="ticket_manager"

# Run formatting with black
$PYTHON_EXEC black $PROJECT_FOLDER

# Run lint with flake8
$PYTHON_EXEC flake8 $PROJECT_FOLDER

