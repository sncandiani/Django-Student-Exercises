from django.db import models
from django.urls import reverse

class Cohort(models.Model):

    name = models.CharField(max_length = 50)

    class Meta:
        verbose_name = ("Cohort")
        verbose_name_plural = ("Cohorts")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Cohort_detail", kwargs={"pk": self.pk})