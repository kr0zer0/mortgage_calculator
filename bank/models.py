from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Bank(models.Model):
    name = models.CharField(max_length=100, unique=True)
    interest_rate = models.IntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(1)]
    )
    maximum_loan = models.PositiveIntegerField()
    minimum_down_payment = models.IntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(1)]
    )
    loan_term = models.IntegerField()

    def __str__(self):
        return self.name
