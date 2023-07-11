# Python-Django_DRF-Django-Rest-Framework_RESTfulAPI-Design
### Django-Rest-Framework is the package for Django to design RESTful API.
### This project shows how to use the DRF with a Character model, with pk, fk and other normal fields.
<br>

<br>

# Requirements
1. You need a Python environment for this project.
2. Please pip install all packages shown in the requirements.txt.
3. For more details about Django REST framework, please see [DRF doc]: www.django-rest-framework.org/#installation

<br>

# Serializer
Serializing is to convert Django model data type to a readable type for front-end, like JSON, XML and so on. The reverse of serialization will convert a input data to a reasonable formay in Django database.

In the application, we use DRF serializer to realize this function. Serializers are sealed in DRF package, you can import it with:
```python
from rest_framework import serializers
```

As a sealed function, it may not explain what it does in ```serializers.py```. So, here's an example to show how serializer work on Character class in Django sqlite3 database to JSON type:
* Go to your Django root dir in cmd and type the following to enter the Django console (if you are using PyCharm, you can directly open this console):

```cmd
  python manage.py shell
```

* In the opened shell (still the cmd, but you are in the shell now), type:
```python
>>> from drf_restapi.models import Character
>>> from django.core import serializers
>>> serializers.serialize('json', Character.objects.all())
```


* With my test data, I get:
```
'[{"model": "drf_restapi.character", "pk": 1, "fields": {"name": "Gary", "intro": "Test Charac", "level": "1", "health": "100", "attack": "10.00", "createdAt": "2023-07-06T05:19:34.133Z", "chaClass": 1}}]'
```
* In a Django App, you will need ```serializers.py``` in the root dir of that app, like in this project.


<br>

# Api_view
You have multiple ways to write API views. Following is one of the most basic one, I'll use it as an example here, you can access all other ways' details after the example.

You can use api_view to deal with GET, POST or other requests with serializer to mulnipulate the database, following is a POST to add data to Django databse, at ```localhost/character/fbv/lst/```:
```
POST /character/fbv/lst/
HTTP 201 Created
Allow: GET, POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": 2,
    "name": "Lucian",
    "intro": "Test Charac",
    "level": "10",
    "health": "300",
    "attack": "30.00",
    "createdAt": "2023-07-07T03:15:17.569816Z",
    "chaClass": 1
}
```

<br>


| View Style | request.method | URL |
|:---------:|:---------:|:---------:|
| Function Based View | GET/POST | localhost/fbv/lst/ |
| Function Based View | GET/PUT/DELETE/... | localhost/fbv/detail/<int:pk>/ |
| Class Based View | GET/POST | localhost/cbv/lst/ |
| Class Based View | GET/PUT/DELETE/... | localhost/cbv/lst/<int:pk>/ |
| Genetic Class Based View | GET/POST | localhost/gcbv/lst/ |
| Genetic Class Based View | GET/PUT/DELETE/... | localhost/gcbv/lst/<int:pk>/ |
| DRF Viewsets | ALL | localhost/viewsets/method(/<int:pk>/) |

<br>
<br>

# AUTHENTICATION

## Basic Way

Django normally use 
```python
'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ]
```
to realize authentication. 
* Basic auth is just for testing, not for production environment.
* Session auth is used when using methods that will activate session, which is a temporary user info on the web server side.
* Token auth is a common useful authentication method. Django will automatically generate a token with the project when it's started.

## DRF Token Authorization
* To use DRF token auth, you need to put it in installed_app in settings.py
  ```python
  INSTALLED_APPS = [
    ...,
    'rest_framework.authtoken', # DRF token authentication
    ...,
  ]
  ```
*
