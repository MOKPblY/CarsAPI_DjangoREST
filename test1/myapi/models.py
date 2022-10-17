from django.db import models

# Create your models here.

class Color(models.Model):
    color = models.CharField(max_length=15, help_text="Hex color")

    def __str__(self):
        return self.color

class Vendor(models.Model):
    vendor = models.CharField(max_length=30, help_text="Auto vendor")
    def __str__(self):
        return self.vendor

class Model(models.Model):
    model = models.CharField(max_length=20, help_text="Model auto")
    vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE)

    def __str__(self):
        return self.model

class Order(models.Model):
    color = models.ForeignKey('Color', on_delete=models.CASCADE) #???
    model = models.ForeignKey('Model', on_delete=models.CASCADE)
    qty = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('qty',)

    def __str__(self):
        return str(self.id)