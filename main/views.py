from django.http import HttpResponse
from django.shortcuts import render,redirect

from .forms import ContactForm
from .models import Contact


# Create your views here.
def main_page(request):
    return render(request, 'main/index.html')


def contact(request):
    form = ContactForm(request.POST)
    if request.POST and form.is_valid():
        form.save()
        return redirect('show_contacts')
    ctx = {'form': form}
    return render(request, 'main/contact.html',ctx)



def show_contacts(request):
    contacts = Contact.objects.all()
    ctx = {'contacts': contacts}
    return render(request, 'main/all_contacts.html',ctx)
