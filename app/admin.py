from django.contrib import admin
from .models import User,Visit,Video

# Register your models here.

admin.site.register(User)
admin.site.register(Visit)
admin.site.register(Video)