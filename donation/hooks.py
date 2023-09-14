from django.dispatch import receiver
from django.views.decorators.csrf import csrf_exempt
from paypal.standard.ipn.signals import valid_ipn_received
from paypal.standard.models import ST_PP_COMPLETED


@csrf_exempt
@receiver(valid_ipn_received)
def paypal_hook(sender, **kwargs):
    ipn_obj = sender
    # print("this is a hook")
    return
