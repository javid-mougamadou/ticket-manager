#!/usr/bin/env sh

PYTHON_EXEC=${PYTHON_EXEC:-"uv run"}
DJANGO_SETTINGS_MODULE=${DJANGO_PROJECT_NAME:-ticket_manager.settings}
PROJECT_FOLDER="ticket_manager"

# Run coverage
$PYTHON_EXEC pytest --cov=$PROJECT_FOLDER

