# accounts/urls.py
from django.urls import path

from . import views


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('not-found-error/', views.show404, name='show404'),
    path('internal-server-error/', views.show500, name='show500'),
    path('shop/<pk>/', views.shop, name='shop'),
    path('my-cart/', views.cart, name='cart'),
    path('products-list/', views.products_all, name='products_all'),
    path('contact/', views.contact, name='contact'),
    path('specifications/', views.specific, name='specific'),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('upload/', views.model_form_upload, name='model_form_upload'),
    path('order-success/', views.order_success, name='order_success'),
    path('contact-success/', views.contact_success, name='contact_success'),
]