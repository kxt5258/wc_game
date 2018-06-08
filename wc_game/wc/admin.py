from django.contrib import admin
from .models import Country, Player, Match, Team
# Register your models here.

admin.site.register(Country)
admin.site.register(Player)
admin.site.register(Team)
admin.site.register(Match)
