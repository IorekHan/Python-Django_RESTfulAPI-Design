from django.utils.ipv6 import is_valid_ipv6_address
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Character
from .serializers import ChaSerializer0


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
