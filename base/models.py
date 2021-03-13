from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    udpated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']
