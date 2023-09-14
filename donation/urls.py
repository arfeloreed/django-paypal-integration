from django.urls import include, path

from . import views

# my app url paths
urlpatterns = [
    path("", views.index, name="home"),
    path("payment-successful/", views.payment_successful, name="payment-successful"),
    path("payment-failed/", views.payment_failed, name="payment-failed"),
    path("paypal/", include("paypal.standard.ipn.urls")),
]
