from datetime import datetime
import pytz
from django.contrib import admin
from .models import Group, Message


class GroupAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'uuid', 'timesince']
    search_fields = ['title', 'description', 'owner.username']

    @staticmethod
    def timesince(obj):
        now = datetime.now(pytz.utc)
        date = obj.date.replace(tzinfo=pytz.utc)
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
class MessageAdmin(admin.ModelAdmin):
    list_display = ['sender', 'group', 'sender', 'timesince']

    @staticmethod
    def timesince(obj):
        now = datetime.now(pytz.utc)
        date = obj.date.replace(tzinfo=pytz.utc)
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


admin.site.register(Group, GroupAdmin)
admin.site.register(Message, MessageAdmin)
