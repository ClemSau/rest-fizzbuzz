FROM python:3.8-slim

WORKDIR /app
COPY requirements /app/requirements
RUN pip install -r requirements/tests.txt
RUN pip install uvicorn gunicorn uvloop httptools
COPY . /app/

EXPOSE 8000
ENV PYTHONUNBUFFERED 1
CMD ["gunicorn", "rest_fizzbuzz.asgi:application", "-k", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:8000"]
