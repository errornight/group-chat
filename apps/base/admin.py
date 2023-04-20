from django.contrib import admin
from .models import User
from datetime import datetime
import pytz

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'time_since']
    search_fields = ['username']

    @staticmethod
    def time_since(obj):
        now = datetime.now(pytz.utc)
        date = obj.date_joined.replace(tzinfo=pytz.utc)
        elapsed = now - date
        days = elapsed.days
        hours, remainder = divmod(elapsed.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        if days > 0:
            return f"{days} days, {hours} hours ago"
        elif hours > 0:
            return f"{hours} hours, {minutes} minutes ago"
        else:
            return f"{minutes} minutes ago"

admin.site.register(User, CustomUserAdmin)
