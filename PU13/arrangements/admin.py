from django.contrib import admin
from .models import Challenge


class ChallengeAdmin(admin.ModelAdmin):
    list_display = ('challenge_name', 'rec_user_level', 'created_at', 'created_by')


admin.site.register(Challenge, ChallengeAdmin)
