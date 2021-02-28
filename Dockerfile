FROM python:3.9.2-alpine

RUN mkdir -p /home/test_app

COPY ./app/ /home/test_app

WORKDIR /home/test_app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["gunicorn", "hello:app"]

