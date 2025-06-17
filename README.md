# Ticket Manager

## Table of Contents

- [Note](#note)
- [Changelog](#changelog)
- [Features](#features)
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Getting started](#getting-started)
- [Endpoints](#endpoints)
- [Testing](#testing)
- [Versioning](#versioning)
- [Contact](#contact)

## Note

This repository contains the source code of the API of Ticket Manager.

## Changelog

### 1.0.0

- Django/DRF added
- Ticket models/endpoints
- Test cases added
- Swagger/Redoc integration

## Features

* Manage tickets

## Dependencies

* Docker
* Python 3.12
* Django 5.2
* Postgres 17.1 (optional)

* UV/Poetry

## Installation

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Installation with Docker Compose


1) Just run the local docker compose file. It will build the image for the service *api*, *db* (optional)

```bash
docker compose up -d
```

2) You can now enter inside the container

```bash
docker compose exec api bash
```

## Getting Started

### Configuration

1) Copy the template settings file *local_settings.py.template* into *local_settings.py* (optional).

```bash
cp local_settings.py.template local_settings.py
```

2) Ensure that the following variables are correctly set in the file *settings.py* or *local_settings.py*


```bash
# Postgres Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
```

3) You can change the path to media, static and upload folders :

```
# Static files (CSS, JavaScript, Images)
STATIC_ROOT = '/data/static/'
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = '/data/media/'
```

### Runserver


1) Go inside the backend container

```bash
docker compose exec api bash
```

2) You can run the start-development.sh script in order to run the local server.

```bash
bash scripts/start-development.sh
```

Otherwise you can manually apply the migration files and launch the runserver command.

```bash
uv run manage.py migrate # Apply migrations
uv run manage.py runserver 0.0.0.0:8000 # Run local server
```

Now the Django server is exposed on http://localhost:8000

You can have access to the django admin interface through http://localhost:8000/admin.

You can have access to the api endpoints through http://localhost:8000/api/v1.

You can have access to the redoc (Swager UI) through http://localhost:8000/redoc.

## Endpoints

This API currently exposes theses endpoints :

* Tickets : /api/tickets/

## Linting

We use PEP8 and Flake8/Black as tools for analyzing source code to flag programming errors, bugs, stylistic errors, and suspicious constructs.

```bash
bash scripts/run-linting.sh
```

## Testing

We use pytest and pytest-django in order to run unit, integration and E2E tests. You can edit conftest.py in order to manage test fixtures.

You can run the test-development.sh script.

```bash
sh scripts/run-pytest.sh
sh scripts/run-coverage.sh
```

Otherwise you can manually launch the pytest command.

```bash
pytest
pytest --cov=ticket_manager # With coverage
```

## Versioning

We use http://semver.org/ for versioning.

## Contact

* Javid Mougamadou (javid.mougamadou2@gmail.com)
