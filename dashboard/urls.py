
from django.urls import  path
from .views import dashboard,categories


urlpatterns = [
    
    path('', dashboard, name='dashboard'),
    path('categories/', categories, name='categories'),
    
] 