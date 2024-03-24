from django.contrib import admin
from .models import Chat, Message
# Register your models here.
class ChatAdmin(admin.ModelAdmin):
    list_display = ('id', 'receiver', 'recipient')
    readonly_fields = ('id',)  # If id is included here, it will be read-only

admin.site.register(Chat, ChatAdmin)
admin.site.register(Message)
