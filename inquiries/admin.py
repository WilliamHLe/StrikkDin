from django.contrib import admin
from .models import Inquiries

class MessagesAdmin(admin.ModelAdmin):
    """
    List_display skal kunne vise felter som Admin kan se på siden sin.
    """
    list_display = ('text_from', 'created_at','subject', 'description')

"""
Kobler Inquiries-modellen til MessagesAdmin-klassen.
"""
admin.site.register(Inquiries, MessagesAdmin)