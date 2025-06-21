from django.contrib import admin
from .models import *

admin.site.register(Hardware)
admin.site.register(HardwareCategory)
admin.site.register(Project)
admin.site.register(HardwareHistory)

