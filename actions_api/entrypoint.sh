#!/bin/sh

# если база еще не запущена
echo "DB not yet run..."

# Проверяем доступность хоста и порта
while ! nc -z $DB_HOST $DB_PORT; do
  sleep 0.1
done

echo "DB did run."

python3 app.py

exec "$@"