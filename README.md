1. Запускаем redis командой:
docker-compose up
2. Запускаем celery.
В другой вкладке терминала запускаем celery командой:
celery -A main.celery_app worker
3. Запускаем приложение main.py.
