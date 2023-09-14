from django.shortcuts import render
from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm

from .forms import CustomPayPalPaymentsForm


# Create your views here.
# view route for my home page
def index(request):
    # functions for the paypal button
    paypal_dict = {
        "business": "reedpogi@business.com",
        "amount": "5.00",
        "notifu_url": request.build_absolute_uri(reverse("paypal-ipn")),
        "return": request.build_absolute_uri(reverse("payment-successful")),
        "cancel_return": request.build_absolute_uri(reverse("payment-failed")),
    }

    # creating the form instance
    form = PayPalPaymentsForm(initial=paypal_dict)

    return render(
        request,
        "donation/index.html",
        {
            "form": form,
        },
    )


# view route for payment successful page
def payment_successful(request):
    return render(
        request,
        "donation/payment-successful.html",
    )


#  view route for payment failure page
def payment_failed(request):
    return render(
        request,
        "donation/payment-failed.html",
    )
