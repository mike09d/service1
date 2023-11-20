# FROM python:3.8.12-slim-bullseye
FROM python:3.10

# Set wordir
WORKDIR /code

# add requirements
COPY requirements.txt . 

# install requirements
RUN pip3 install  --no-cache-dir -r requirements.txt 

COPY . .

# open port
EXPOSE 80

# Init command
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]

