FROM python:3.10

ENV PYTHONDONTWIRTEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /app


COPY requirements.txt .

RUN pip install -r requirements.txt


COPY . /app/

CMD ["bash", "-c", "python3 manage.py migrate && python3 manage.py collectstatic --no-input && gunicorn --reload -b 0.0.0.0:8000 config.wsgi --workers 1 --timeout 300 --log-level DEBUG"]

