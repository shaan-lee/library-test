import logging
from celery import Celery

app = Celery("tasks", broker="amqp://localhost:5672")


@app.task
def print_log():
    logging.info("logging")
    print("print")


# print_log.delay()

# app.conf.beat_schedule = {
#    "run-me-every-10-sec": {
#        "task": "tasks.test_celery.print_log",
#        "schedule": 10.0,
#    }
# }
