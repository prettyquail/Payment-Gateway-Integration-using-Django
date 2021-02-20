from django.urls import path
from .views import home,success,first

urlpatterns = [
    path('',first ,name='first'),
    path('success/' , success , name='success'),
    path('home/', home , name='home'),
]