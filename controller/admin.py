from django.contrib import admin
from .models import FanButtonModel, DuctButtonModel, Mode, ModeElements, DuctPosition, SensorData

admin.site.register(FanButtonModel)
admin.site.register(DuctButtonModel)
admin.site.register(Mode)
admin.site.register(ModeElements)
admin.site.register(DuctPosition)
admin.site.register(SensorData)