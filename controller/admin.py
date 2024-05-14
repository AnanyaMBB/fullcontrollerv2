from django.contrib import admin
<<<<<<< HEAD
from .models import FanButtonModel, DuctButtonModel, Mode, ModeElements, DuctPosition, DuctMaxValue
=======
from .models import FanButtonModel, DuctButtonModel, Mode, ModeElements, DuctPosition, SensorData1, SensorData2, SensorData3, SensorData4, SensorData4, SensorData5, SensorData6
>>>>>>> 8bcf087cd6757c6c5072a51d2816405af8ac4e99

admin.site.register(FanButtonModel)
admin.site.register(DuctButtonModel)
admin.site.register(Mode)
admin.site.register(ModeElements)
admin.site.register(DuctPosition)
<<<<<<< HEAD
# admin.site.register(SensorData)
admin.site.register(DuctMaxValue)
=======
admin.site.register(SensorData1)
admin.site.register(SensorData2)
admin.site.register(SensorData3)
admin.site.register(SensorData4)
admin.site.register(SensorData5)
admin.site.register(SensorData6)
>>>>>>> 8bcf087cd6757c6c5072a51d2816405af8ac4e99
