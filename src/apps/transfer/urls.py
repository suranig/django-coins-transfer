from django.urls import path

from .views import TransferListCreateAPIView


urlpatterns = [
    path('transfers/',
         TransferListCreateAPIView.as_view(),
         name='transfers'),
]
