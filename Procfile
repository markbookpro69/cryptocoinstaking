web: gunicorn staking.wsgi --log-file -
celery: celery -A staking.celery worker -l info
celerybeat: celery -A staking beat -l INFO 
celeryworker: celery -A staking.celery worker & celery -A staking beat -l INFO & wait -n