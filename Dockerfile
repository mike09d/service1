# FROM python:3.8.12-slim-bullseye
FROM python:3.9.16-bullseye
# open port
EXPOSE 5002

# add requirements
COPY requirements.txt /app/requirements.txt

# install requirements
RUN pip install  --no-cache-dir -r app/requirements.txt

# copy source code
COPY . /app/app
# set workdir
WORKDIR /app/app

# Init command
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5002"]


