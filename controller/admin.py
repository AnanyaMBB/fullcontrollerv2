from django.contrib import admin
from .models import FanButtonModel, DuctButtonModel, Mode, ModeElements, DuctPosition, SensorData1, SensorData2, SensorData3, SensorData4, SensorData5, SensorData6, DuctMaxValue

admin.site.register(FanButtonModel)
admin.site.register(DuctButtonModel)
admin.site.register(Mode)
admin.site.register(ModeElements)
admin.site.register(DuctPosition)
admin.site.register(SensorData1)
admin.site.register(SensorData2)
admin.site.register(SensorData3)
admin.site.register(SensorData4)
admin.site.register(SensorData5)
admin.site.register(SensorData6)
admin.site.register(DuctMaxValue)
