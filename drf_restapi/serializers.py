from django import forms
from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Character



class ChaFrom(forms.ModelForm):

    class Meta:
        model = Character
        fields = ('name', 'intro', 'level', 'health', 'attack', 'chaClass')



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'



class ChaSerializer0(serializers.ModelSerializer):

    chaClasses = serializers.ReadOnlyField(source = 'chaClasses.username')

    class Meta:
        model = Character
        #fields = ('name', 'intro', 'level', 'health', 'attack', 'chaClass')
        fields = '__all__'


class ChaSerializer(serializers.HyperlinkedModelSerializer):
   chaClasses = serializers.ReadOnlyField(source = 'chaClasses.username')

   class Meta:
       model = Character
       #fields = ('name', 'intro', 'level', 'health', 'attack', 'chaClass')
       fields = '__all__'