from django.urls import path
from . import views
urlpatterns = [
  path('main/', views.main),
  path('insert/', views.insert),
  path('show/', views.show),
  path('signup/',views.signup),
  path('signin/', views.signin),
  path('signout/', views.signout),
  path('id_check/', views.id_check),
  path('change/', views.change),
]