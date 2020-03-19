from django.contrib import admin
from .models import Challenge, KnitNight


class ChallengeAdmin(admin.ModelAdmin):
    list_display = ('challenge_name', 'rec_user_level', 'created_at', 'created_by')


class KnitAdmin(admin.ModelAdmin):
    list_display = ('knit_name', 'time', 'created_at', 'created_by')


admin.site.register(KnitNight, KnitAdmin)
admin.site.register(Challenge, ChallengeAdmin)
