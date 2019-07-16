from django.contrib import admin
from . import models
##导入本app的模型

# Register your models here.
admin.site.register(models.User)