from django.contrib import admin
from .models import MyProject, MyService
# Register your models here.
admin.site.register(MyProject)
admin.site.register(MyService)