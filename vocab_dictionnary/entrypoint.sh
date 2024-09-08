#!/bin/sh

echo "Waiting for PostgreSQL to be ready..."

while ! pg_isready -h db -p 5432 -U postgres; do
  sleep 1
done

echo "PostgreSQL is ready. Applying database migrations..."
python3 manage.py migrate

if [ $? -eq 0 ]; then
  echo "Migrations applied successfully"
else
  echo "Failed to apply migrations"
  exit 1
fi

echo "Starting server..."
exec "$@"
