#!/bin/sh

echo "Applying database migrations..."
  python3 manage.py migrate

if [ $? -eq 0 ]; then
  echo "Migrations applied successfully"
else
  echo "Failed to apply migrations"
fi

echo "Starting server..."
exec "$@"
