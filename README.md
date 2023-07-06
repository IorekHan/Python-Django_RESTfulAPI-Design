# Python-Django_RESTfulAPI-Design

## Requirements
1. You need a Python environment for this project.
2. Please pip install all packages shown in the requirements.txt.
3. For more details about Django REST framework, please see [DRF doc]: www.django-rest-framework.org/#installation

## Serialize
Serializing is to convert Django model data type to a readable type for front-end, like JSON, XML and so on.

Here's an example to serialize Character class in Django sqlite3 database to JSON type:
* Go to your Django root dir in cmd and type the following to enter the Django console (if you are using PyCharm, you can directly open this console):

  '''
  python manage.py shell
  '''

* In the opened shell (still the cmd, but you are in the shell now), type:
'''python
>>> from drf_restapi.models import Character
>>> from django.core import serializers
>>> serializers.serialize('json', Character.objects.all())
'''
* With my test data, I get:
'''
'[{"model": "drf_restapi.character", "pk": 1, "fields": {"name": "Gary", "intro": "Test Charac", "level": "1", "health": "100", "attack": "10.00", "createdAt": "2023-07-06T05:19:34.133Z", "chaClass": 1}}]'
'''
 
