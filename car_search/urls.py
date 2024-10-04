from django.urls import path
from .views import CarSearchViewSet

urlpatterns = [
    path('search/', CarSearchViewSet.as_view({'get': 'list'}), name='car-search'),
]
