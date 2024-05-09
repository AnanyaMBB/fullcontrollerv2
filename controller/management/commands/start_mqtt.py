# myapp/management/commands/start_mqtt.py

from django.core.management.base import BaseCommand
import paho.mqtt.client as mqtt
from controller.models import SensorData1, SensorData2, SensorData3, SensorData4, SensorData5, SensorData6
from django.utils.timezone import now
from datetime import datetime 

class Command(BaseCommand):
    help = 'Starts an MQTT client to listen for incoming data and saves it to the database'

    def handle(self, *args, **options):
        client = mqtt.Client()

        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                self.stdout.write(self.style.SUCCESS('Connected to MQTT Broker!'))
                # Specify the topic you want to subscribe to
                client.subscribe("sensor1/data")  
                client.subscribe("sensor2/data")  
                client.subscribe("sensor3/data")
                client.subscribe("sensor4/data")
                client.subscribe("sensor5/data")
                client.subscribe("sensor6/data")
                
            else:
                self.stdout.write(self.style.ERROR('Failed to connect, return code %d\n', rc))

        def on_message(client, userdata, msg):
            self.stdout.write(self.style.SUCCESS(f'Received message on topic {msg.topic}'))
            # Assuming the payload is a JSON string with temperature and humidity data
            # import json
            # data = json.loads(msg.payload.decode('utf-8'))
            # temperature = data.get('temperature')
            # humidity = data.get('humidity')

           
            # print(f"Receieved data : {msg.payload.decode('utf-8')}")
            data_lst =  msg.payload.decode('utf-8').split(' ')
            
            # Save to database
            try: 
                if msg.topic == "sensor1/data":
                    sensorData = SensorData1(timestamp=datetime.datetime.now(),
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
                    
                elif msg.topic == "sensor2/data":
                    sensorData = SensorData2(timestamp=datetime.datetime.now(),
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

                elif msg.topic == "sensor3/data":
                    sensorData = SensorData3(timestamp=datetime.datetime.now(),
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

                elif msg.topic == "sensor4/data":
                    sensorData = SensorData4(timestamp=datetime.datetime.now(),
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

                elif msg.topic == "sensor5/data":
                    sensorData = SensorData5(timestamp=datetime.datetime.now(),
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

                elif msg.topic == "sensor6/data":
                    sensorData = SensorData6(timestamp=datetime.datetime.now(),
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
