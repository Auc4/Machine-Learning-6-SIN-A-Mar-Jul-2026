FROM python:3.12-slim

# System dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install UV (fast Python package manager)
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:${PATH}"

WORKDIR /app

# Create the virtual environment
RUN uv venv .venv
ENV VIRTUAL_ENV=/app/.venv
ENV PATH="/app/.venv/bin:${PATH}"

# Install dependencies — note the --python flag, mandatory in Docker
# because there is no `source .venv/bin/activate` step that persists across layers
COPY pyproject.toml uv.lock* /app/
RUN uv pip install --python /app/.venv/bin/python \
    pandas \
    scikit-learn \
    matplotlib \
    seaborn \
    numpy \
    ipykernel \
    jupyter

# Copy project files
COPY . /app/

CMD ["bash"]
