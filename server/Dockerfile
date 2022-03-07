FROM python:3.8

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src/ .

EXPOSE 8888

# TODO: Change this if this would go into production as this a dev serve
CMD [ "python", "./server.py" ]
