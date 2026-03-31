FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    curl \
    git \
    git-lfs \
    && rm -rf /var/lib/ap/lists/*

RUN git lfs install --system
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:$PATH"
WORKDIR /app
RUN uv venv .auca_venv
COPY requirements.txt .
RUN uv pip install --python .auca_venv/bin/python -r requirements.txt
ENV VIRTUAL_ENV=/app/.auca_venv
ENV PATH="/app/.auca_venv/bin:$PATH"