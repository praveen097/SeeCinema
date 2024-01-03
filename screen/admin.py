from django.contrib import admin
from django.apps import apps
# Register your models here.
myapp = apps.get_app_config('screen')
for model in myapp.get_models():
    admin.site.register(model)