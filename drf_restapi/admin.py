from django.contrib import admin
from .models import  Character
# Register your models here.

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name', 'intro', 'level', 'health', 'attack', 'chaClass')
    search_fileds = list_display
    list_filter = list_display
