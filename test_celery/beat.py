from celery import Celery
from test_celery.test_celery import app


app.conf.beat_schedule = {
    "run-me-every-10-sec": {
        "task": "test_celery.test_celery.print_log",
        "schedule": 10.0,
    }
}
