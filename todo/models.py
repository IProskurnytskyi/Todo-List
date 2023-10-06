from django.db import models


class Task(models.Model):
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(null=True, blank=True)
    is_completed = models.BooleanField()
    tags = models.ManyToManyField("Tag", related_name="tasks")

    def __str__(self):
        return self.content


class Tag(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name
