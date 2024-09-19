from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=256)
    user = models.CharField(max_length=64)

    class Meta:
        db_table = "Tasks"