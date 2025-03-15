from django.contrib import admin
from . import models

admin.site.register(models.Match)
admin.site.register(models.Player)
admin.site.register(models.Tournament)
admin.site.register(models.Tournament_Bracket)
admin.site.register(models.Player_Point)
admin.site.register(models.Tournament_Player)



