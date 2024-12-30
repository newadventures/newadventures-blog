FROM python:3.12.8-slim

WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# install dependencies
COPY requirements.in /app/requirements.in
COPY requirements_dev.in /app/requirements_dev.in
RUN pip install --upgrade pip
RUN pip install uv
RUN uv pip compile requirements.in --output-file requirements.txt --emit-index-url
RUN uv pip install --system --no-cache-dir -r requirements.txt
RUN uv pip compile requirements_dev.in --output-file requirements_dev.txt --emit-index-url
RUN uv pip install --system --no-cache-dir -r requirements_dev.txt



# copy project
COPY . /app/