FROM python:3.12.10 AS base-dev

WORKDIR /data/

RUN curl -Ls https://astral.sh/uv/install.sh | bash

ENV PATH="/root/.local/bin:$PATH"

COPY pyproject.toml .
COPY uv.lock .

RUN uv sync

CMD ["/bin/bash",  "scripts/start-development.sh"]