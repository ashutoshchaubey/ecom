# accounts/views.py
from django import forms
from django.urls import reverse_lazy
from django.contrib.auth import login as auth_login
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from .forms import ContactForm, SignUpForm#, DocumentForm#, BlouseForm, ShirtsForm, SkirtsForm, GownsForm
from django.views import generic
from .models import Products, Blouse, Shirts, Skirts, Gowns, Profile, Specifications, Cart, Content, Order, OrderItem
from django.shortcuts import render, redirect, get_object_or_404

def show404(request):
    return render(request, '404.html')

def show500(request):
    return render(request, '500.html')

def products_all(request):
    product_list = Products.objects.all()
    filtered_orders = Order.objects.filter(is_ordered=True)
    current_order_products = []
    if filtered_orders.exists():
        user_order = filtered_orders[0]
        user_order_items = user_order_items.all()
        current_order_products = [product.product for product in user_order_items]
    context = {
        'product_list': product_list,
        'current_order_products': current_order_products,
    }
    return render(request, 'product-list.html', context)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            cont = form.save()
            cont.refresh_from_db()
            from_email = request.POST.get('from_email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            cont.save()
            return redirect('contact_success')

    return render(request, "contact.html", {'form': form})

def contact_success(request):
    return render(request, 'contact_success.html')

def shop(request, pk=None, *args, **kwargs):
    product_item = get_object_or_404(Products, pk=pk)
    type_of_item = product_item.items_type
    context = {
        'product_item': product_item,
    }
    return render(request, 'shop.html', context)

def cart(request, pk=None, *args, **kwargs):
    if Products.in_cart is True:
        selected_product = Products.objects.get(in_cart=True)
        if selected_product.in_cart == True:
            product_item_type = selected_product.items_type
            product_image = selected_product.image
            product_title = selected_product.title
            product_price = selected_product.price
        selected_product_price = product_price
        service_charge = (5*selected_product_price)/100
        if selected_product_price>10.00:
            discount_new = (3*selected_product_price)/100
            shipping_charge = 2.00
        else:
            discount_new = 0.00
            shipping_charge = 4.00
        total = round((float(selected_product_price) + float(discount_new) + float(service_charge) + shipping_charge), 2)
        product_quantity = 1
        product_discount = round(discount_new,2)
        product_service_charge = round(service_charge, 2)
        product_shipping_charge = round(shipping_charge,2)
        context = {
            'product_item_type': product_item_type,
            'selected_product': selected_product,
            'total': total, 
            'product_quantity': product_quantity, 
            'product_image': product_image, 
            'product_title': product_title,
            'selected_product_price': selected_product_price,
            'product_discount': product_discount,
            'product_service_charge': product_service_charge,
            'product_shipping_charge' : product_shipping_charge,
        }
        return render(request, 'my_cart.html', context)
    else:
        error = 'Oops ... Your Cart is Empty'
        context = {
            'error': error
        }
        return render(request, 'my_cart.html', context)

def add_to_cart(request, pk=None, *args, **kwargs):
    if Products.in_cart == False:
        product_item_to = Products.get_object_or_404(pk=pk)
        change_cart_status = product_item_to.in_cart(True)
        context = {
            'change_cart_status': change_cart_status,
        }
        return render(request, 'product-list.html', context)
    else:
        return render(request, 'product-list.html')

def order_success(request):
    return render(request, 'order_success.html')

def model_form_upload(request):
    if request.method == 'POST':
        if request.POST.get('image') and request.POST.get('name_of_item'):
            new_item = Content()
            new_item.title = request.POST.get('title')
            new_item.name_of_item = request.POST.get('name_of_item')
            new_item.save()
            return render(request, 'upload_design.html')
    else:
        return render(request, 'upload_design.html')

def specific(request, pk=None, *args, **kwargs):
    # if Products.items_type == 'Blouse':
    #     # if request.method == 'GET':
    #     #     form = forms.ModelForm(request.POST)
    #     # else:
    #     #     form = forms.ModelForm(request.POST)
    #     #     if form.is_valid():
    #     #         specific_products = form.save()
    #     #         specific_products.refresh_from_db()
    #     #         product_blouse = Products.objects.get(items_type = Blouse)
    #     #         specific_blouse = Blouse.objects.all()
    #     #         blouse_length = form.cleaned_data.get('specific_blouse.length')
    #     #         blouse_half_length = form.cleaned_data.get('specific_blouse.half_length')
    #     #         blouse_ub_length = form.cleaned_data.get('specific_blouse.ub_length')
    #     #         blouse_ub_width = form.cleaned_data.get('specific_blouse.ub_width')
    #     #         blouse_sleeve = form.cleaned_data.get('specific_blouse.sleeve')
    #     #         blouse_round_sleeve = form.cleaned_data.get('specific_blouse.round_sleeve')
    #     #         blouse_tf_sleeve = form.cleaned_data.get('specific_blouse.tf_sleeve')
    #     #         blouse_long_sleeve = form.cleaned_data.get('specific_blouse.long_sleeve')
    #     #         blouse_shoulder = form.cleaned_data.get('specific_blouse.shoulder')
    #     #         specific_products.save()
    return render(request, 'specifications.html')

