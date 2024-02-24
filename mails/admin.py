from django.contrib import admin

from mails.models import Client


# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('pk','email', 'last_name', 'first_name', 'father_name','comment',)
    list_filter = ('email','last_name',)

