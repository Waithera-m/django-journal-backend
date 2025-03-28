FROM python:3.11

WORKDIR /app

ENV PYHTONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

COPY requirements.txt  /app/

COPY . /app/

RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
