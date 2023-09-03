# specify start image
FROM python

# all commands start from this directory
WORKDIR /app

# copy all files from this folder to working directory (ignores files in .dockerignore)
COPY . .

RUN pip install poetry
ENV PATH="${PATH}:/root/.poetry/bin"
RUN "poetry install"
EXPOSE 4999

# set the start command
CMD [ "poetry run python -m flask run --host=0.0.0.0 --port=4999"]
