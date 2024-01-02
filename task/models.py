from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField() 
    status = models.CharField(max_length=20, choices=[('not_started', 'Not Started'), ('in_progress', 'In Progress'), ('completed', 'Completed')])
    order = models.IntegerField()

    def __str__(self):
        return self.title