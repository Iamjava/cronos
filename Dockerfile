FROM python:3.10
ENV POETRY_VERSION=1.5.1
ENV POETRY_VENV=/opt/poetry-venv

# Install poetry separated from system interpreter
RUN python3 -m venv $POETRY_VENV \
    && $POETRY_VENV/bin/pip install -U pip setuptools \
    && $POETRY_VENV/bin/pip install poetry==${POETRY_VERSION}

# Add `poetry` to PATH
ENV PATH="${PATH}:${POETRY_VENV}/bin"
WORKDIR /app

COPY poetry.lock pyproject.toml ./
RUN poetry install

# Run your app
COPY . /app
EXPOSE 4999
# set the start command
CMD [ "poetry", "run", "python", "-m flask", "run", "--host=0.0.0.0", "--port=4999"]
