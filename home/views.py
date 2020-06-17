from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Photo
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm


def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            sender = form.cleaned_data['sender']
            message = 'Номер телефона: ' + form.cleaned_data['phone'] + '   ' + 'Текст сообщения: ' + form.cleaned_data['message']
            copy = form.cleaned_data['copy']

            recipients = ['decorex@decorexx.ru', 'Decorexx@mail.ru']
            if copy:
                recipients.append(sender)
            try:
                send_mail(subject, message, sender, recipients)
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return render(request, 'home/thanks.html')
    else:
        form = ContactForm()
    return render(request, 'home/index.html', {'form': form})


def projects(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            sender = form.cleaned_data['sender']
            message = 'Номер телефона: ' + form.cleaned_data['phone'] + '   ' + 'Текст сообщения: ' + form.cleaned_data['message']
            copy = form.cleaned_data['copy']

            recipients = ['decorex@decorexx.ru', 'Decorexx@mail.ru']
            if copy:
                recipients.append(sender)
            try:
                send_mail(subject, message, sender, recipients)
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return render(request, 'home/thanks.html')
    else:
        form = ContactForm()
    data = {
    'pub_projects': Project.objects.order_by('-pub_date'),
    'photo_projects': Photo.objects.order_by('-pub_date'),
    'form': form,
    }

    return render(request, 'home/projects.html', data)


def about(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            sender = form.cleaned_data['sender']
            message = 'Номер телефона: ' + form.cleaned_data['phone'] + '   ' + 'Текст сообщения: ' + form.cleaned_data['message']
            copy = form.cleaned_data['copy']

            recipients = ['decorex@decorexx.ru', 'Decorexx@mail.ru']
            if copy:
                recipients.append(sender)
            try:
                send_mail(subject, message, sender, recipients)
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return render(request, 'home/thanks.html')
    else:
        form = ContactForm()
    
    return render(request, 'home/about.html', {'form': form})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            sender = form.cleaned_data['sender']
            message = 'Номер телефона: ' + form.cleaned_data['phone'] + '   ' + 'Текст сообщения: ' + form.cleaned_data['message']
            copy = form.cleaned_data['copy']

            recipients = ['decorex@decorexx.ru', 'Decorexx@mail.ru']
            if copy:
                recipients.append(sender)
            try:
                send_mail(subject, message, sender, recipients)
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return render(request, 'home/thanks.html')
    else:
        form = ContactForm()
    
    return render(request, 'home/contact.html', {'form': form})
