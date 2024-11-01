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

class SensorData1(models.Model):
    timestamp = models.DateTimeField(null=True, blank=True)
    temperature = models.FloatField()
    humidity = models.FloatField()
    pressure = models.FloatField()
    altitude = models.FloatField()
    lux = models.FloatField()
    dustDensity = models.FloatField()
    windSpeed = models.FloatField(null=True, blank=True)
    status = models.CharField(max_length=200, null=True, blank=True)
    aqi = models.FloatField(null=True, blank=True)
    tvoc = models.FloatField(null=True, blank=True)
    eco2 = models.FloatField(null=True, blank=True)



    # rature': data_lst[0],
    #         'pressure': data_lst[1],
    #         'altitude': data_lst[2],
    #         'humidity': data_lst[3],
    #         'lux': data_lst[4],
    #         'dustDensity': data_lst[5],
    #         'windSpeed': data_lst[6],
    #         'status': data_lst[7],
    #         'aqi': data_lst[8],
    #         'tvoc': data_lst[9],
    #         'eco2': data_lst[1

class SensorData2(models.Model):
    timestamp = models.DateTimeField(null=True, blank=True)
    temperature = models.FloatField()
    humidity = models.FloatField()
    pressure = models.FloatField()
    altitude = models.FloatField()
    lux = models.FloatField()
    dustDensity = models.FloatField()
    windSpeed = models.FloatField(null=True, blank=True)
    status = models.CharField(max_length=200, null=True, blank=True)
    aqi = models.FloatField(null=True, blank=True)
    tvoc = models.FloatField(null=True, blank=True)
    eco2 = models.FloatField(null=True, blank=True)


class SensorData3(models.Model):
    timestamp = models.DateTimeField(null=True, blank=True)
    temperature = models.FloatField()
    humidity = models.FloatField()
    pressure = models.FloatField()
    altitude = models.FloatField()
    lux = models.FloatField()
    dustDensity = models.FloatField()
    windSpeed = models.FloatField(null=True, blank=True)
    status = models.CharField(max_length=200, null=True, blank=True)
    aqi = models.FloatField(null=True, blank=True)
    tvoc = models.FloatField(null=True, blank=True)
    eco2 = models.FloatField(null=True, blank=True)


class SensorData4(models.Model):
    timestamp = models.DateTimeField(null=True, blank=True)
    temperature = models.FloatField()
    humidity = models.FloatField()
    pressure = models.FloatField()
    altitude = models.FloatField()
    lux = models.FloatField()
    dustDensity = models.FloatField()
    windSpeed = models.FloatField(null=True, blank=True)
    status = models.CharField(max_length=200, null=True, blank=True)
    aqi = models.FloatField(null=True, blank=True)
    tvoc = models.FloatField(null=True, blank=True)
    eco2 = models.FloatField(null=True, blank=True)


class SensorData5(models.Model):
    timestamp = models.DateTimeField(null=True, blank=True)
    temperature = models.FloatField()
    humidity = models.FloatField()
    pressure = models.FloatField()
    altitude = models.FloatField()
    lux = models.FloatField()
    dustDensity = models.FloatField()
    windSpeed = models.FloatField(null=True, blank=True)
    status = models.CharField(max_length=200, null=True, blank=True)
    aqi = models.FloatField(null=True, blank=True)
    tvoc = models.FloatField(null=True, blank=True)
    eco2 = models.FloatField(null=True, blank=True)


class SensorData6(models.Model):
    timestamp = models.DateTimeField(null=True, blank=True)
    temperature = models.FloatField()
    humidity = models.FloatField()
    pressure = models.FloatField()
    altitude = models.FloatField()
    lux = models.FloatField()
    dustDensity = models.FloatField()
    windSpeed = models.FloatField(null=True, blank=True)
    status = models.CharField(max_length=200, null=True, blank=True)
    aqi = models.FloatField(null=True, blank=True)
    tvoc = models.FloatField(null=True, blank=True)
    eco2 = models.FloatField(null=True, blank=True)

class DuctMaxValue(models.Model):
    max_value = models.FloatField(null=True, blank=True)

class LightModes(models.Model):
    mode_id = models.AutoField(primary_key=True)
    mode_name = models.CharField(max_length=200, null=True, blank=True)
    on_lights = models.CharField(max_length=400, null=True, blank=True)
    color = models.CharField(max_length=200, null=True, blank=True)
    brightness = models.IntegerField(null=True, blank=True)

class PowerIPS(models.Model):
    sensor_ip = models.CharField(max_length=200, null=True, blank=True)
    pi_ip = models.CharField(max_length=200, null=True, blank=True)
    duct_1_ip = models.CharField(max_length=200, null=True, blank=True)
    duct_2_ip = models.CharField(max_length=200, null=True, blank=True)
    duct_3_ip = models.CharField(max_length=200, null=True, blank=True)
    duct_4_ip = models.CharField(max_length=200, null=True, blank=True)

class Co2Offset(models.Model):
    offset = models.FloatField(null=True, blank=True)
    