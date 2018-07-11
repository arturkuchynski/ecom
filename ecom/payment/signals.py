from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
import weasyprint
from io import BytesIO
from orders.models import Order


# TODO: Mark order as paid
def payment_notification(sender, **kwargs):
    ipn_obj = sender
    if ipn_obj.payment_status == ST_PP_COMPLETED:
        # payment was successful
        order = get_object_or_404(Order, id=ipn_obj.invoice)

        # mark the order as paid
        order.paid = True
        print('payment saved as paid')
        order.save()

        # create invoice e-mail
        subject = 'My Shop - Invoice nr. {}'.format(order.id)
        message = 'Please, find attached the invoice for your recent purchase.'
        email = EmailMessage(subject, message, 'archeski.dk@gmail.com', [order.email])

        # generate PDF
        html = render_to_string('orders/order/pdf.html', {'order': order})
        out = BytesIO()
        stylesheets = [weasyprint.CSS(settings.STATIC_URL + 'static_dev/css/pdf.css')]
        weasyprint.HTML(string=html).write_pdf(out,
                                               stylesheets=stylesheets)
        # attach PDF file
        email.attach('order_{}.pdf'.format(order.id),
                     out.getvalue(),
                     'application/pdf')
        # send e-mail
        email.send()


valid_ipn_received.connect(payment_notification)
