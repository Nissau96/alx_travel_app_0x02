# listings/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ListingViewSet, BookingViewSet, InitiatePaymentView


router = DefaultRouter()
router.register(r'listings', ListingViewSet, basename='listing')
router.register(r'bookings', BookingViewSet, basename='booking')


urlpatterns = [
    path('', include(router.urls)),
    path('initiate-payment/', InitiatePaymentView.as_view(), name='initiate-payment'),
]