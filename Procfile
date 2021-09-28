server: cd server && gunicorn explore.wsgi
worker: cd server && celery -A explore worker 
client: cd client && yarn build && yarn start 