from django.contrib import admin
from .models import Messages1

class MessagesAdmin(admin.ModelAdmin):
    list_display = ('text_from', 'created_at','subject', 'description')

admin.site.register(Messages1, MessagesAdmin)