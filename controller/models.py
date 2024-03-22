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

class DuctPosition(models.Model):
    btnID = models.CharField(max_length=200)
    position = models.FloatField()

class Mode(models.Model):
    mode_id = models.AutoField(primary_key=True)
    mode_name = models.CharField(max_length=200, null=True, blank=True)
    mode_description = models.CharField(max_length=200, null=True, blank=True)

class ModeElements(models.Model):
    mode_id = models.ForeignKey(Mode, on_delete=models.CASCADE)
    mode_identifier = models.CharField(max_length=200)
    mode_command = models.CharField(max_length=20, null=True, blank=True)
    mode_type = models.CharField(max_length=5, null=True, blank=True)  # fan or duct

