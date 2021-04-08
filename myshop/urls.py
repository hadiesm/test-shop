from django.urls import path
from . import views


app_name = 'shop'

urlpatterns = [
    path('',views.main_page,name = 'main'),
    path('products/',views.product_list_page,name='list'),
    path('products/<slug:category_slug>',views.product_list_page,name='list_by_category'),
    path('product/<slug:product_slug>/',views.product_detail_page,name='detail'),
    path('contact-us/',views.contact_page,name='about'),
    path('about/',views.about_page,name='about'),
    path('privacy/',views.privacy_page,name='privacy'),
    path('terms/',views.terms_page,name='terms'),
    path('payment-policy/',views.payment_policy_page,name='payment_policy'),
    path('shipping-policy/',views.shipping_policy_page,name='shipping_policy'),
    path('return-policy/',views.return_policy_page,name='return_policy'),
    path('my-account/',views.my_account_page,name='my_account'),
]

