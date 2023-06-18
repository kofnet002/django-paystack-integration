from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PaymentForm
from decouple import config
from .models import Payment
from django.contrib import messages


# Create your views here.
def initiate_payment(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        payment_form = PaymentForm(request.POST)
        if payment_form.is_valid():
            payment = payment_form.save()
    
            context={
                'payment' : payment,
                'paystack_pulic_key' : config('PAYSTACK_PUBLIC_KEY')
            }

            return render(request, 'paystack/confirm_payment.html', context)

    else:
        context = {
            'payment_form' : PaymentForm()
        }
    return render(request, 'paystack/payment.html', context)



def verify_payment(request: HttpRequest, ref: str) -> HttpResponse:
    payment = get_object_or_404(Payment, ref=ref)

    verifying_payment = payment.verify_payment()

    if verifying_payment:
        messages.success(request, "Verification successful!")
    else:
        messages.error(request, "Verification failed!")
    return redirect('payment')