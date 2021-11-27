from django.db import models

# Create your models here.
class Todo(models.Model):
    task_name = models.CharField(max_length=300)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
