from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage

def contact(request):
    contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)

        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            message = request.POST.get('message', '')

            email = EmailMessage(
                'Mensaje de contacto recibido',
                'Mensaje enviado por {} <{}>:\n\n{}'.format(name, email, message),
                email,
                ['f5c2c3d7128df3@inbox.mailtrap.io'],
                reply_to=[email],
            )

            try:
                email.send()
                return redirect(reverse('contact') + '?ok')
            except:
                return redirect(reverse('contact') + '?error')

    return render(request, 'contact/contact.html', {'form': contact_form})









