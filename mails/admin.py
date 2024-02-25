from django.contrib import admin

from mails.models import Client, Message


# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('pk','email', 'last_name', 'first_name', 'father_name','comment',)
    list_filter = ('email','last_name',)
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('pk','title', 'body',)
    search_fields = ('title', 'body',)
    list_filter = ('title',)

