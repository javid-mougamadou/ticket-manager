#!/usr/bin/env sh

PYTHON_EXEC=${PYTHON_EXEC:-"uv run"}
DJANGO_SETTINGS_MODULE=${DJANGO_PROJECT_NAME:-ticket_manager.settings}
PROJECT_FOLDER="ticket_manager"

# Run test cases
$PYTHON_EXEC pytest

