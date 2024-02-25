from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView

from blog.models import Blog
from mails.forms import ClientForm, MessageForm
from mails.models import Client, Message


class IndexView(TemplateView):
    template_name = 'mails/index.html'
    extra_context = {
        'title': 'Главная',
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Blog.objects.all()[:3]
        return context_data


def contacts(request):
    context = {
        'title': "Контакты",
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f"{name} ({phone}, {email}): {message}")

    return render(request, 'mails/contacts.html', context)


class ClientListView(ListView):
    model = Client
    extra_context = {
        'title': "Клиенты сервиса ",
    }


class ClientDetailView(DetailView):
    model = Client


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mails:client_list')


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mails:client_list')

class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('mails:client_list')

class MessageListView(ListView):
    model = Message
    extra_context = {
        'title': "Сообщения для рассылки ",
    }


class MessageDetailView(DetailView):
    model = Message


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mails:message_list')


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mails:message_list')

class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('mails:message_list')
