# Syncware

### How to run

Create a DB in Postgres with the following items:

  Name of device, Signals, RelationshipToOtherDevices

data:

  1.	'Robot Yellow' , {'battery level' : 70. 0, 'Position': (17, 34.5, 1.2)}, {'plugs': ['Hostserver' ], 'receives': [ ]}

  2.	'Hostserver' , {'Ram' : 85.4}, {'plugs': ['Robot Red' ], 'receives' : ['Robot Yellow']}

  3.	'Robot Red', {'battery level' : 30.5, 'position' : (24.5, 47, 0.4)}, {'plugs' : [ ], 'receives' : ['Hostserver']

Change the setting.py according to you db settings

  DATABASES = {
  
      'default': {
      
          'ENGINE': 'django.db.backends.postgresql',
          
          'NAME': 'syncware', --> DB name
          
          'USER': 'postgres', --> default user name
          
          'PASSWORD': '*****', --> password
          
          'HOST': '127.0.0.1', --> HOST
          
          'PORT': '5432',      --> default port
          
      }
      
  }


Make sure that the name of the project folder is same in the "INSTALLED APP" section in settings page

    INSTALLED_APPS = [
    
      'syncware', --> name of the app
      
      'django.contrib.admin',
      
      'django.contrib.auth',
      
      'django.contrib.contenttypes',
      
      'django.contrib.sessions',
      
      'django.contrib.messages',
      
      'django.contrib.staticfiles',
  
    ]

Create a virtual environment and activate the environment

    python3 -m venv env

    env\scripts\activate
  
Go to the folder in cmd then follow the following steps

Install the required packages

    python -m pip install django==2.2.11

    python -m pip install psycopg2
  
Run the app

    python manage.py runserver


