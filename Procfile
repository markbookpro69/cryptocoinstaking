web: gunicorn staking.wsgi --log-file -
worker: celery -A staking worker --beat