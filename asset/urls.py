from django.urls import include, path
from . import views


urlpatterns = [
    path('server/', views.server, name="server"),
    path('group_config/', views.group_config, name="group_config"),

]