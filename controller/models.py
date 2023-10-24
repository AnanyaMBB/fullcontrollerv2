from django.db import models

class FanButtonModel(models.Model):
    btnID = models.CharField(max_length=200)
    model = models.CharField(max_length=200)


class DuctButtonModel(models.Model):
    btnID = models.CharField(max_length=200)
    model = models.CharField(max_length=200)


class AcLastCommand(models.Model):
    btnID = models.CharField(max_length=200)
    command = models.CharField(max_length=200)
