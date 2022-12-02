from django.db import models


class Goal(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    is_year = models.BooleanField(default=False)
    is_month = models.BooleanField(default=False)
    is_week = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
