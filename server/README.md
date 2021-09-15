# Explore

## Dependencies
### Create your virtualenv
```bash
pip install virtualenv
virtualenv .env
source .env/bin/activate
```
### Install dependencies
```bash
pip install -r requirements.txt
```
  

## Launch the project
### Front & API
```bash
./manage.py runserver
```

### Celery workers
Several workers are needed to get data from Strava and process some operations. 

**- RabbitMQ server**
```bash
/usr/local/opt/rabbitmq/sbin/rabbitmq-server
```
**- Celery worker**
```bash
celery -A explore worker -l INFO
```
**- Celery beat** (for cronjob tasks)
```bash
celery -A explore beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
```