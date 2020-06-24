from django.contrib import admin
from .models import Cachorro, Gato, petPerdido, petAchado, petEncontrado, Voluntario
# Register your models here.

admin.site.register(Voluntario)
admin.site.register(Cachorro)
admin.site.register(Gato)
admin.site.register(petPerdido)
admin.site.register(petAchado)
admin.site.register(petEncontrado)
