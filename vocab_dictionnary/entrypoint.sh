#!/bin/sh

echo "Waiting for database..."
while ! nc -z db 5432; do
  sleep 1
done

echo "Applying database migrations..."
python3 manage.py migrate

if [ $? -eq 0 ]; then
  echo "Migrations applied successfully"
else
  echo "Failed to apply migrations"
fi

echo "Starting server..."
exec "$@"
