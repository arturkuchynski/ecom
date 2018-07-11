from celery import task
from django.core.mail import EmailMessage
from .models import Order


@task
def order_created(order_id):
    """
    Task to send an e-mail notification when an order is 
    successfully created.
    """

    order = Order.objects.get(id=order_id)
    subject = 'Order nr. {}'.format(order.id)
    message = 'Dear {},\n\nYou have successfully placed an order.\
                  Your order id is {}.'.format(order.first_name,
                                               order.id)
    msg = EmailMessage(subject,
                       message,
                       'Bookstore archeski.dk@gmail.com',
                       to=[order.email])
    msg.send()
    file = open('../worker.txt', 'w')
    file.write('Mail sent')
    file.close()
