# usage
- run rabbitmq with docker
```
docker run rabbitmq
```

- run worker.py 

```
celery -A test_celery.worker worker
```

- run beat.py

```
celery -A test_celery.beat beat
```