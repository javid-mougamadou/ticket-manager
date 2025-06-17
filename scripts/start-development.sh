#!/usr/bin/env sh

PYTHON_EXEC=${PYTHON_EXEC:-"uv run python"}
RUNSERVER_BIND_PORT=8000
RUNSERVER_BIND_HOST=0.0.0.0
DJANGO_SETTINGS_MODULE=${DJANGO_PROJECT_NAME:-ticket_manager.settings}

# Remove Sqlite database file
if [ -f "db.sqlite3" ]; then
  echo "Removing existing db.sqlite3..."
  rm db.sqlite3
fi

# Apply migrations
$PYTHON_EXEC manage.py migrate

# Run development server at localhost:8000
$PYTHON_EXEC manage.py runserver $RUNSERVER_BIND_HOST:$RUNSERVER_BIND_PORT
