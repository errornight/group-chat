from django.db import models
import uuid

class Group(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=420, blank=True, null=True)
    owner = models.ForeignKey('base.User', on_delete=models.PROTECT)
    members = models.ManyToManyField('base.User', related_name='joined_groups')
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)     # so we do not use main 'id' field.
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Message(models.Model):
    sender = models.ForeignKey('base.User', on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='messages')
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:60]
