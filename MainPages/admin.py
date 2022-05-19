from django.contrib import admin

from .models import *
# Register models here.
admin.site.register([Teacher, Courses, Rate])