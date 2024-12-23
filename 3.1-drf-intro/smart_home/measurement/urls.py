from django.urls import path

from measurement import views

urlpatterns = [
    path('sensors/', views.SensorListCreateApiView.as_view(), name='sensor_list'),
    path('sensors/<int:pk>/', views.SensorRetrieveUpdateApiView.as_view(), name='sensor_detail'),
    path('measurements/', views.MeasurementCreateApiView.as_view(), name='create_measurement'),
]
