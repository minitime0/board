from django.urls import path
from . import views
urlpatterns = [
  path('main/', views.main),
  path('json/', views.json),
  path('insert/', views.insert),
  path('show/', views.show),
  path('army_shop/', views.army_shop),

  path(
    'army_shop/<int:year>/<int:month>/', 
    views.army_shop2),
]
#문자는 Str armyshop은 여러개 존재하지 못함
