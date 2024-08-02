# from django.core.management.base import BaseCommand
# from django.utils.timezone import make_aware
# from datetime import timedelta
# import pytz
# from controller.models import SensorData1

# class Command(BaseCommand):
#     help = 'Update timestamps from UTC to GMT+9 for SensorData1'

#     def handle(self, *args, **options):
#         seoul_timezone = pytz.timezone('Asia/Seoul')
#         updated_count = 0

#         for record in SensorData1.objects.all():
#             if record.timestamp:
#                 # Convert UTC to GMT+9
#                 utc_timestamp = record.timestamp.replace(tzinfo=pytz.utc)
#                 gmt9_timestamp = utc_timestamp.astimezone(seoul_timezone)

#                 # Update the record with the new timestamp
#                 record.timestamp = gmt9_timestamp
#                 record.save()
#                 updated_count += 1

#         self.stdout.write(self.style.SUCCESS(f'Successfully updated {updated_count} records.'))


from django.core.management.base import BaseCommand
from django.utils import timezone
from controller.models import SensorData1, SensorData2, SensorData3, SensorData4, SensorData5, SensorData6

class Command(BaseCommand):
    help = 'Update timestamps from UTC to GMT+9 for all sensor data'

    def handle(self, *args, **options):
        # List of all sensor data models
        models = [SensorData1, SensorData2, SensorData3, SensorData4, SensorData5, SensorData6]
        total_updated = 0

        # Process each model
        for model in models:
            updated_count = 0
            # Update each record in the model
            for record in model.objects.all():
                if record.timestamp:
                    # Make the timestamp timezone-aware (assumes it's in UTC)
                    aware_utc_timestamp = timezone.make_aware(record.timestamp, timezone=timezone.utc)
                    # Convert to Asia/Seoul timezone
                    local_timestamp = aware_utc_timestamp.astimezone(timezone.pytz.timezone('Asia/Seoul'))
                    
                    # Update the record with the new timestamp
                    record.timestamp = local_timestamp
                    record.save()
                    updated_count += 1

            model_name = model.__name__
            self.stdout.write(self.style.SUCCESS(f'Updated {updated_count} records in {model_name}.'))
            total_updated += updated_count

        self.stdout.write(self.style.SUCCESS(f'Total records updated across all models: {total_updated}'))
