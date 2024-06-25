FROM python:3.12

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

ENV DJANGO_SETTINGS_MODULE=vocab_dictionnary.settings

COPY ./entrypoint.sh .
RUN chmod +x /app/entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]


CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
