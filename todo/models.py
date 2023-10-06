from django.db import models


class Task(models.Model):
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(null=True, blank=True)
    is_completed = models.BooleanField()
    tags = models.ManyToManyField("Tag", related_name="tasks", blank=True)

    class Meta:
        ordering = ("is_completed", "datetime")


class Tag(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name
