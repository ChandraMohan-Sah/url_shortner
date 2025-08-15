lets design a database :

attributes 
1 = id
2 = title 
3 = images
4 = duration 
5 = description 
6 = likes
7 = dislikes 
8 = isoriginal 
9 = duration 
10 = releasedate



1. Featured video 
2. Featured today 
3. top picks	   
4. popular movies 
5. exclusive videos 
6. streaming :
7. tv shows :
8. top rated shows : 
10. coming soon :
11. editors picks : 
12. news :
13. celebrity :
 
----------------------------------------------------------------------------

    create django project with mydjango

    re-structure:
        1. apps -> put all apps


        2. in settings.py :
                import sys
                sys.path.insert(0, os.path.join(BASE_DIR, "apps"))

 
        3. in global urls.py :
                path( ...., apps.)


        4. in each app inside apps.py 
                name = 'apps.app1...'

           in settings.py 
                INSTALLED_APPS = [
                        apps.app1_client ,
                        ...
                ]
        
  
        5.config/settings -> put base.py, dev.py, prod.py 
        config -> global asgi.py, urls.py, wsgi.py 


        6. manage.py changes : 
            'config.settings.dev'
 

        7. in base.py:
            ROOT_URLCONF = 'config.urls'

            WSGI_APPLICATION = 'config.wsgi.application'


        8. create an app named core :
                to hold all management commnds for db 


        9. creating separate database for different apps
                - create folder named datatabase 
                - go to dev.py
                        DATABASES = {
                        'default': {
                                'ENGINE': 'django.db.backends.sqlite3',
                                'NAME': BASE_DIR / 'database' /'default.sqlite3',
                        },
                        'user_db': {
                                'ENGINE': 'django.db.backends.sqlite3',
                                'NAME': BASE_DIR / 'database' / 'user_db.sqlite3',
                        },
                        'media_db': {
                                'ENGINE': 'django.db.backends.sqlite3',
                                'NAME': BASE_DIR / 'database' / 'media_db.sqlite3', 
                        }
                        # add more databases as needed
                        }
                
                - base.py 
                        DATABASE_ROUTERS = ['shared.db_router.AppDatabaseRouter']

                - write coded shared/db_router.py
                - write code for : global_project/migrate_all_db.py 

        10. 
--------------------------------------------------------------------------------

python manage.py migrate app1_media --database=media_db.sqlite3



---------------------------------------------------------------------------------
Approach :
 
  Stage I : ( Gathering Information )
	
	1. Gather Client Requirement 

	2. Figureout Core Services required 

	3. Create a Falsy Prototype (Paper Work : UML Based if possible with Appropriate Design Pattern)

	4. Design Database Schema 





  Stage II : (Beginner Works )

	1. API Creation (coding stuff : models, serializers, views,  urls )

	2. Adding permission , authentication , throttling 

	3. Basic Optimization + Most Do Works : ( DB_QUERYSET optimize, pagination ) , ( filtering , ordering, searching )

	4. Document API using ( swagger + sphinex (if needed) )

	5. Coding Stuff : API Testing 

	6. Follow CI/CD Pipeline : and deploy the project (Initial Stage)





  Stage III : (Intermediate Works)- [Analysis : based on your computer RAM (say 8GB)]
	
	1. Figure out slow and duplicate queries increacing latency 

	2. Profile HTTP requests, track DB queries, and analyze performance.

	3. Load Test :  Simulate user traffic and measure RPS/response times.

	4. Performance Enhancement Tools
			- Redis: for caching frequent queries, sessions

			- Celery + RabbitMQ/Redis: for background tasks
			
			- Async Views / Channels: for real-time apps or non-blocking performance
			
			- Optimize ORM usage and indexing in DB
		



 Stage IV : Deploy the App 

	1. Make Sure Confidentiality is maintained (like .env for secret keys)

	2. Use any cloud services (like pythonanywhere.com , AWS )


 Stage IV : Dockerize the App 
	
	1. Write a Dockerfile 


 Stage V  : Orchestration | Horizontal Scaling using Kubernetes



 Stage VI : Versioning of Services [Replace or Renew the existing Services]



 Stage VII : Monitoring and Logging : Grafana , Prometheus
  


 Stage IX  : Keep Growing (Apply CICD pipeline) 




---------------
    """
    Model representing a user's rating and optional review for a specific episode.

    Fields:
        episode (ForeignKey): Reference to the Episode being reviewed.
        user_episode_review (ForeignKey): Reference to the User who submitted the review.
        rating (PositiveIntegerField): Numeric rating for the episode (1-10).
        review (CharField): Optional textual review (max 200 characters).
        active (BooleanField): Indicates if the review is active.
        created (DateTimeField): Timestamp when the review was created.
        updated (DateTimeField): Timestamp when the review was last updated.

    Methods:
        __str__(): Returns a string representation showing the episode title and its rating.
    """
--------------------





       