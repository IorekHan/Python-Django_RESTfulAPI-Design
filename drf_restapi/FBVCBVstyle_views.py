from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.utils.decorators import method_decorator

import json
# Create your views here.


Cha_dict = {
    'name' : 'John',
    'level' : '2',
    }

# Django FBV style API
@csrf_exempt
def cha_lst(request):


    if request.method == 'GET':
        return JsonResponse(Cha_dict)
        # return HttpResponse(json.dumps(Cha_dict), content_type = 'application/json')

    if request.methos == 'POST':
        character = json.loads(request.body.decode('utf-8'))
        return JsonResponse(character, safe=False)



# Django CBV style API
@method_decorator(csrf_exempt, name='dispatch')
class Cha_lst(View):

    def get(self, request):
        return JsonResponse(Cha_dict)

    def post(self, request):
        character = json.loads(request.body.decode('utf-8'))
        return JsonResponse(character, safe=False)