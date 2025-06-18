PYTHON_EXEC = uv run
PROJECT_FOLDER = ticket_manager
DJANGO_SETTINGS_MODULE = ticket_manager.settings
RUNSERVER_BIND_HOST = 0.0.0.0
RUNSERVER_BIND_PORT = 8000

.DEFAULT_GOAL := help

.PHONY: help
help:
	@echo "Available commands:"
	@echo "  make test         - Run unit tests"
	@echo "  make cov          - Run tests with coverage"
	@echo "  make format       - Format code using Ruff"
	@echo "  make lint         - Lint code using Ruff"
	@echo "  make black        - Format code using Black only"
	@echo "  make run          - Start the Django development server"
	@echo "  make reset-db     - Delete db.sqlite3 and run migrations"
	@echo "  make check        - Format + Lint using Ruff"
	@echo ""

.PHONY: test
test:
	$(PYTHON_EXEC) pytest

.PHONY: cov
cov:
	$(PYTHON_EXEC) pytest --cov=$(PROJECT_FOLDER)

.PHONY: format
format:
	$(PYTHON_EXEC) ruff check --fix $(PROJECT_FOLDER)

.PHONY: lint
lint:
	$(PYTHON_EXEC) ruff check $(PROJECT_FOLDER)

.PHONY: check
check: format lint

.PHONY: black
black:
	$(PYTHON_EXEC) black $(PROJECT_FOLDER)

.PHONY: run
run:
	$(PYTHON_EXEC) manage.py runserver $(RUNSERVER_BIND_HOST):$(RUNSERVER_BIND_PORT)

.PHONY: reset-db
reset-db:
	@if [ -f "db.sqlite3" ]; then \
		echo "Removing db.sqlite3..."; \
		rm db.sqlite3; \
	fi
	$(PYTHON_EXEC) manage.py migrate
