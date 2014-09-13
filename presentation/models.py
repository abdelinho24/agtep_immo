from django.db import models

# Create your models here.


class Offer(models.Model):
    """
    Represents an land's Offer  Django model.
    """
    Title = models.CharField(max_length=40)
    Price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    Surface = models.IntegerField()
    Description = models.TextField()

