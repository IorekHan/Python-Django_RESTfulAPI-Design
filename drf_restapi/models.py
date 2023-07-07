from django.db import models
from django.conf import settings

# Create your models here.

class Character(models.Model):
    name = models.CharField(max_length = 255, unique = True)
    intro = models.TextField()
    level = models.DecimalField(max_digits = 5, decimal_places=0)
    health = models.DecimalField(max_digits = 10, decimal_places=0)
    attack = models.DecimalField(max_digits = 10, decimal_places=2)
    createdAt = models.DateTimeField(auto_now_add=True)

    chaClass = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Character_info'
        verbose_name_plural = verbose_name
        ordering = ('level',)

    def __str__(self):
        return self.name


Character.objects.all() # Serialize, Django data type -> Frontend data type(JSON/XML...)