from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('profile/', views.create_profile, name='create_profile')

]
