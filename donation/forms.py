from paypal.standard.forms import PayPalPaymentsForm


# custom paypal form layout
class CustomPayPalPaymentsForm(PayPalPaymentsForm):
    def get_html_submit_element(self):
        return """<button type="submit">Continue on PayPal website</button>"""
