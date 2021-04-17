from datetime import timedelta

from django.db import models


class DirectionModel(models.Model):
    spec_name = models.TextField(null=True)
    prof_name = models.TextField(null=True)
    colledge_name = models.TextField()

    base_study_time = models.DurationField(default=timedelta(days=1100))
    short_study_time = models.DurationField(default=timedelta(days=356))

    def __repr__(self):
        return self.name

    def __str__(self):
        return f'{self.colledge_name} - {self.spec_name} - {self.prof_name}'

    class Meta():
        verbose_name = "Directions"
        verbose_name_plural = "Direction"