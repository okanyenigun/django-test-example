from django.urls import path
from home.views import HomeView, DetailView
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<int:pk>', DetailView.as_view(), name='detail'),
]