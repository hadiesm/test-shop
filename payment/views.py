from django.shortcuts import render , redirect , get_object_or_404
import braintree
from django.conf import settings
from orders.models import Order
from .tasks import payment_completed
# Create your views here.

gateway = braintree.BraintreeGateway(
  braintree.Configuration(
    environment=braintree.Environment.Sandbox,
    merchant_id='nscdq5xq7fdtt4m8',
    public_key='wnws56drb3m72dx6',
    private_key='6e3a2c6a16e6d0ea9f2b25aadfaf31e4'
  )
)

def payment_pocess(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order,id=order_id)
    total_cost = order.get_total_cost()

    if request.method == 'POST':
        nonce = request.POST.get('payment_method_nonce', None)
        result = gateway.transaction.sale({
            'amount': f'{total_cost:.2f}',
            'payment_method_nonce': nonce,
            'options':{
                'submit_for_settlement': True
            }
        })
        if result.is_success:
            order.paid = True
            order.braintree_id = result.transaction.id
            order.save()
            payment_completed.delay(order.id)
            return redirect('payment:done')
        else:
            return redirect('payment:canceled')
    else:
        client_token = gateway.client_token.generate()
        return render(request,'payment/process.html',{'order':order,
                                                      'client_token':client_token})

def payment_done(request):
    return render(request,'payment/done.html')

def payment_canceled(request):
    return render(request,'payment/canceled.html')

