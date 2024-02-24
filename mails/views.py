from django.shortcuts import render
from django.views.generic import TemplateView

from blog.models import Blog


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
