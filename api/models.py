from django.db import models

class Make(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Model(models.Model):
    name = models.CharField(max_length=100)
    make = models.ForeignKey(Make, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class CarType(models.Model):
    name = models.CharField(max_length=100)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
