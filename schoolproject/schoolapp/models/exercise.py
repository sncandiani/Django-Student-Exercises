from django.db import models
from django.urls import reverse

class Exercise(models.Model):

    name = models.CharField(max_length = 50)
    language = models.CharField(max_length = 50)

    class Meta:
        verbose_name = ("Exercise")
        verbose_name_plural = ("Exercises")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Exercise_detail", kwargs={"pk": self.pk})