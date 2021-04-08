from celery import shared_task
from django.core.mail import send_mail
from .models import Order


@shared_task
def order_created (order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Order No. {order.id}'
    message = f'Dear {order.first_name},'f'You have successfully placed an order.'\
        f'Your order ID is : {order.id}.'
    sent_mail = send_mail(subject,message,'hadi@shop.com',[order.email])
    return sent_mail