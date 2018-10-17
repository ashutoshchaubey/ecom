from django.shortcuts import render
from .forms import BillingForm, DocumentForm

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = BillingForm(request.POST)
        if form.is_valid():
            bill = form.save()
            bill.refresh_from_db()
            bill.full_name = form.cleaned_data.get('full_name')
            bill.email = form.cleaned_data.get('email')
            bill.billing_addr = form.cleaned_data.get('billing_addr')
            bill.shipping_addr = form.cleaned_data.get('shipping_addr')
            bill.pincode = form.cleaned_data.get('pincode')
            bill.phone_number = form.cleaned_data.get('phone_number')
            bill.save()
            return redirect('order_success')
    else:
        form = BillingForm()
    return render(request, 'billing/home.html', {'form': form})

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'upload_design.html', {
        'form': form
    })