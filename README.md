> After months of lockdown, running in circles around your block, always
> taking the same route, knowing every rock, every sidewalk or every
> pothole... Now it's time for the great outdoors! Go conquer new virgin
> territories, climb that hill or take that dead end... in short, get
> off the beaten track!
# Explore
Explore is an open-source conquest game that allows you to to **challenge your friends around a GPS map**. Each map is divided into "tiles" (a zone of 1km2). Each map is divided into "tiles" (an area of 1km square). As soon as you **sync your favorite GPS application** after going for a run, you'll have all the new tiles you've encountered along the way - and that wouldn't be in the possession of one of your friends yet. At the end of the period, the user who has conquered the most zones wins the game!
# Backlog
Explore was developed with **MVP in mind** and is in continuous improvement, both technically and functionally. The next iterations are documented in this [backlog](https://www.notion.so/5bfa8c2e56b44c97ba2dcd6c2d1930da?v=9fffd66b3faa449eb54220378d0ea9b0). 

# Tech stuff
This repository contains both:
-  **`client/`**: the front-end (the registration module, the map, etc.)
- **`server/`**: the back-end (the API consumed by the application and the asynchronous GPS process tasks).

You'll be able to find the running documentation in each directory, but here is the details of the stack used. 
## Server
### Technical stack
- [Django](https://www.djangoproject.com/) with some cool libs (REST framework, AllAuth, etc).
- [Celery](https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html) for each asynchronous tasks.
- [Redis](https://redis.io) as broker manager.  
- [PostGIS](https://postgis.net/) in order to store geospatial data and process them efficiently.
### Main principles

The Django app is divided in several apps:  

 - **`api/`**: All serializers and API views to communicate with the application. 
 - **`core/`**: All models, admin management and global functions. 
 -  **`map/`**: All things related to map processing and GPS parsing. 
 - **`tasks/`**: All Celery tasks to process things asynchronously.
 - **`explore/`**: The default running application.  

### Broker actions
// TBD

## Client
### Technical stack
- NextJS
- Typescript - almost 😅
### Main principles

// TBD
