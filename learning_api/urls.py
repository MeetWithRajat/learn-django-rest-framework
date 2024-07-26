from django.urls import path
from learning_api import views

urlpatterns = [
    path('hello-view/', views.HelloAPIView.as_view())
]
