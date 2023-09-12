from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail

from .forms import ContactUsForm
from .models import Band


def contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz'],
            )
            return redirect('contact_sent')
    else:
        form = ContactUsForm()

    return render(request, 'listings/contact.html', {'form': form})


def contact_sent(request):
    return HttpResponse("Thank you for your message!")

def band_index(request):
    bands = Band.objects.all()
    return render(request, 'listings/band/index.html', {'bands': bands})


def band_detail(request, band_id):
    band = Band.objects.get(id=band_id)
    return render(request, 'listings/band/detail.html', {'band': band})
