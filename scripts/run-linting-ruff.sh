#!/usr/bin/env sh

PYTHON_EXEC=${PYTHON_EXEC:-"uv run"}
PROJECT_FOLDER="ticket_manager"

# Run formatting with ruff
$PYTHON_EXEC ruff check --fix $PROJECT_FOLDER

# Run lint with ruff
$PYTHON_EXEC ruff check $PROJECT_FOLDER
