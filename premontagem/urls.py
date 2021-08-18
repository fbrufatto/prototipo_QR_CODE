from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('add', views.add_bike, name="add_bike"),
    path('bike/qr/<str:pk>', views.qr_code_bike, name="qr_code_bike"),
    path('bike/<str:pk>', views.bike_info, name="bike_info"),
]
