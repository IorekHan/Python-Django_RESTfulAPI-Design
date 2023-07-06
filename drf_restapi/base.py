from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Character
from .serializers import ChaSerializer0


# FBV style
@api_view(['GET', 'POST'])
def cha_lst(request):

    if request.method == 'GET':
        s = ChaSerializer0(instance = Character.objects.all(), many = True)
        return Response(data = s.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
         s = ChaSerializer0(data = request.data)
         if s.is_valid():
             s.save(chaClass = request.user)
             return Response(data = s.data, status = status.HTTP_201_CREATED)
         return Response(s.errors, status = status.HTTP_400_BAD_RESQUEST)