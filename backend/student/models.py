from datetime import timedelta

from django.db import models

from django.conf import settings
from params.models import DirectionModel


class StudentModel(models.Model):
    name = models.TextField()
    lastname = models.TextField()
    fathername = models.TextField()

    birthdate = models.DateField()
    passport = models.TextField()

    phone = models.TextField()

    region = models.TextField(default='г.Томск')
    att_score = models.FloatField()

    is_disabled = models.BooleanField(default=False) # инвалид?
    is_orphan = models.BooleanField(default=False) # сирота?
    is_served = models.BooleanField(default=False) # служил?
    needs_home = models.BooleanField(default=False) # требуется ли общежитие
    is_higher = models.BooleanField(default=False) # после 11го

    male = models.CharField(max_length=1, choices=(
        ('F', 'Female'),
        ('M', 'Male')
    ), default='M')

    # photo ?
    # files
    
    direction = models.ForeignKey(
        DirectionModel,
        on_delete=models.DO_NOTHING,
        related_name='direction',
        null=True
    )
    academ_duration = models.DurationField(default=timedelta()) # длительность академ отпуска
    receipt_date = models.DateField(null=True) # поступление

    user_model = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='user_id'
    )

    def __repr__(self):
        return f'{self.lastname} {self.name} {self.fathername}'

    def __str__(self):
        return f'{self.lastname} {self.name} {self.fathername}'

    class Meta():
        verbose_name = "Students"
        verbose_name_plural = "Student"
