from django.db import models
# Create your models here.


class Branch(models.Model):
    name = models.CharField(max_length=50)
    ifsc = models.IntegerField(max_length=10)
    bank = models.CharField(max_length=50)
    address = models.TextField()
    city = models.CharField(max_length=500)
    district = models.CharField(max_length=500)
    state = models.CharField(max_length=500)

    def __str__(self):
        return "{} - {} - {}".format(self.name, self.city, self.bank)
