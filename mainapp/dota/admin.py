from django.contrib import admin
from dota.models import *
# Register your models here.


@admin.register(Post)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("name","rare","url")#что показать


admin.site.register(Rare)