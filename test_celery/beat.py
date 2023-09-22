from celery.schedules import crontab
from test_celery.test_celery import app


app.conf.beat_schedule = {
    "run-me-every-10-sec": {
        "task": "test_celery.test_celery.print_log",
        "schedule": 10.0,
    },
    "run-me-every-scheduled-time": {
        "task": "teste_celery.test_celery.print_log",
        "schedule": crontab(hour="*", minute=1),
    },
}
