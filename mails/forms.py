from django import forms

from mails.models import Client, Mail, Message


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class ClientForm(StyleFormMixin,forms.ModelForm):
    class Meta:
        model = Client
        # fields = '__all__'
        exclude = ('owner',)


class MailForm(StyleFormMixin,forms.ModelForm):
    class Meta:
        model = Mail
        exclude = ('is_active','owner')
        # fields = '__all__'


class MessageForm(StyleFormMixin,forms.ModelForm):
    class Meta:
        model = Message
        # fields = '__all__'
        exclude = ('owner',)
