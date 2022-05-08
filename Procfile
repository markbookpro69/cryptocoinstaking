web: gunicorn staking.wsgi --log-file -
celeryworker: celery -A staking.celery worker & celery -A staking beat -l INFO & wait -n