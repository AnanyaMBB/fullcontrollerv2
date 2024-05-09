# myapp/management/commands/start_mqtt.py

from django.core.management.base import BaseCommand
import paho.mqtt.client as mqtt
from controller.models import SensorData
from django.utils.timezone import now
from datetime import datetime 

class Command(BaseCommand):
    help = 'Starts an MQTT client to listen for incoming data and saves it to the database'

    def handle(self, *args, **options):
        client = mqtt.Client()

        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                self.stdout.write(self.style.SUCCESS('Connected to MQTT Broker!'))
                client.subscribe("sensor2/data")  # Specify the topic you want to subscribe to
            else:
                self.stdout.write(self.style.ERROR('Failed to connect, return code %d\n', rc))

        def on_message(client, userdata, msg):
            self.stdout.write(self.style.SUCCESS(f'Received message on topic {msg.topic}'))
            # Assuming the payload is a JSON string with temperature and humidity data
            # import json
            # data = json.loads(msg.payload.decode('utf-8'))
            # temperature = data.get('temperature')
            # humidity = data.get('humidity')
            print(f"Receieved data : {msg.payload.decode('utf-8')}")
            print(f"Userdata : {userdata} client: {msg.topic} ")
            data_lst =  msg.payload.decode('utf-8').split(' ')
            print(data_lst) 
            # Save to database
            try: 
                sensorData = SensorData(timestamp=datetime.now(),
                                    temperature=data_lst[2],
                                    humidity=data_lst[3],
                                    pressure=data_lst[4],
                                    altitude=data_lst[1],
                                    lux=data_lst[10],
                                    dustDensity=data_lst[9],
                                    windSpeed=data_lst[5] if data_lst[5]!="nan" else 0,
                                    status=data_lst[0],
                                    aqi=data_lst[8],
                                    tvoc=data_lst[7],
                                    eco2=data_lst[6])

                sensorData.save()
                print("Successfully saved sensor fdata to database!")
            except Exception as e:
                print(f"Exception occured : {e}")
        client.on_connect = on_connect
        client.on_message = on_message

        client.connect("aalsdb.kaist.ac.kr", 1883, 60)
        client.loop_forever()  # Blocks process, consider using loop_start() for non-blocking
