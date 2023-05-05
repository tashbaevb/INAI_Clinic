from django.contrib import admin
from . import models

admin.site.register(models.Contacts)
admin.site.register(models.Doctors)
admin.site.register(models.About)
admin.site.register(models.Comment)
