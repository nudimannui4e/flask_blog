FROM python:alpine
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app
ENTRYPOINT [ "python" ]
CMD [ "init_db.py" ]
ENTRYPOINT FLASK_APP=/app/app.py flask run --host=0.0.0.0
