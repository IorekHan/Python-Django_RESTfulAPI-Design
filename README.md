# Python-Django_DRF-Django-Rest-Framework_RESTfulAPI-Design
### Django-Rest-Framework is the package for Django to design RESTful API.
### This project shows how to use the DRF.
<br>

## Requirements
1. You need a Python environment for this project.
2. Please pip install all packages shown in the requirements.txt.
3. For more details about Django REST framework, please see [DRF doc]: www.django-rest-framework.org/#installation

<br>

## Serialize
Serializing is to convert Django model data type to a readable type for front-end, like JSON, XML and so on. The reverse of serialization will convert a input data to a reasonable formay in Django database.

In the application, we use DRF serializer to realize this function. Serializers are sealed in DRF package, you can import it with:
```python
from rest_framework import serializers
```

As a sealed function may not explain what it does, here's an example to show how serializer work on Character class in Django sqlite3 database to JSON type:
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
