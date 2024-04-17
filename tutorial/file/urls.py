from django.urls import path
from . import views




urlpatterns = [
  path('upload1/', views.upload1),
  path('download/',views.download),
]

