from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Введите имя', 'class': 'form-control'}))
    sender = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Введите электронную почту', 'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Задайте нам вопрос', 'class': 'form-control'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите телефон', 'class': 'form-control'}))
    copy = forms.BooleanField(required=False)


