from blog.views import Home
from django.urls import path
from . import views
app_name = 'blog'
urlpatterns = [
    path('',views.Home,name="home")
]
