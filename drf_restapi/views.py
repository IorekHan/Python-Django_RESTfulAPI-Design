from django.utils.ipv6 import is_valid_ipv6_address
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Character
from .serializers import ChaSerializer0

from rest_framework.views import APIView # For CBV
from rest_framework import generics # GCBV
from rest_framework import viewsets # 


# Auto generate DRF tokne
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender = settings.AUTH_USER_MODEL)
def generate_token(sender, instance = None, created = False, **kwargs):
    if created:
        Token.objects.create(user = instance)




# FBV style
@api_view(['GET', 'POST'])
def cha_lst(request): 
    # For adding or checking database info

    if request.method == 'GET':
        s = ChaSerializer0(instance = Character.objects.all(), many = True)
        return Response(data = s.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
         s = ChaSerializer0(data = request.data)
         if s.is_valid():
             s.save(chaClass = request.user)
             return Response(data = s.data, status = status.HTTP_201_CREATED)
         return Response(s.errors, status = status.HTTP_400_BAD_RESQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def cha_detail(request, pk):

    try:
        character = Character.objects.get(pk=pk)
    except Character.DoesNotExist:
        return Response(data = {'msg' : 'No Character Found'}, status = status.HTTP_404_NOT_FOUND)
    else:
        if request.method == 'GET':
            s = ChaSerializer0(instance = Character, status = status.HTTP_200_OK)
        elif request.method == 'PUT':
            s = ChaSerializer0(instance = Character, data = request.data)
            if s.is_valid():
                s.save()
                return Response(s.data, status = status.HTTP_200_OK)
        elif request.method == 'DELETE':
            Character.delete()
            return Response(status = status.HTTP_204_NO_CONTENT)



# CBV style

class cha_lst1(APIView):
    def get(self, request):
        queryset = Character.objects.all()
        s =  ChaSerializer0(queryset, many = True) # instance is from back-end database
        return Response(s.data, status = status.HTTP_200_OK)
    def post(self, request):
        s = ChaSerializer0(data = request.data) # data is from front-end, need verify
        if s.is_valid():
            s.save(chaClass = self.request.user)
            return Response(s.data, status = status.HTTP_201_CREATED)
        return Response(s.errors, status = status.HTTP_400_BAD_RESQUEST)
    
class cha_detail1(APIView):

    @staticmethod
    def get_obj(pk):
        try:
            return Character.objects.get(pk=pk)
        except Character.DoesNotExist:
            return

    def get(self, request, pk):
        obj = self.get_obj(pk)
        if not obj:
            return Response(data = {'msg': 'No such characters'}, status = status.HTTP_404_NOT_FOUND)
        s = ChaSerializer0(instance = obj)
        return Response(s.data, status = status.HTTP_200_OK)


    def put(self, request, pk):
        obj = self.get_obj(pk)
        if not obj:
            return Response(data = {'msg': 'No such characters'}, status = status.HTTP_404_NOT_FOUND)
        s = ChaSerializer0(instance = obj, data = request.data)
        if s.is_valid():
            s.save()
            return Response(s.data, status = status.HTTP_200_OK)
        return Response(s.errors, status = status.HTTP_400_BAD_RESQUEST)

    def delete(self, request, pk):
        obj = self.get_obj(pk)
        if not obj:
            return Response(data = {'msg': 'No such characters'}, status = status.HTTP_404_NOT_FOUND)

        Character.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)



# Generic Class Based View
class cha_lst2(generics.ListCreateAPIView):
    queryset = Character.objects.all()
    serializer_class = ChaSerializer0

    def p_create(self, serializer):
        serializer.save(chaClass = self.request.user)

class cha_detail2(generics.RetrieveUpdateAPIView):
    queryset = Character.objects.all()
    serializer_class = ChaSerializer0



# DRF viewsets

class cha_viewset(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = ChaSerializer0

    def p_create(self, serializer):
        serializer.save(chaClass = self.request.user)