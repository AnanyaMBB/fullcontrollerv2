from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .models import FanButtonModel, DuctButtonModel, DuctPosition, Mode, ModeElements, DuctMaxValue, LightModes, SensorData1, SensorData2, SensorData3, SensorData4, SensorData5, SensorData6, PowerIPS, Co2Offset
from django.contrib.auth.models import User
from .forms import UserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
import paho.mqtt.client as paho
import json
import time
import datetime
import csv

# broker = '146.190.138.255'
# broker = 'localhost'
broker = '127.0.0.1'
broker = 'aalsdb.kaist.ac.kr'
port = 1883

boolBtnSelectedFan = {
    'east_top_btn_1': 0,
    'east_top_btn_2': 0,
    'east_bottom_btn_1': 0,
    'east_bottom_btn_2': 0,
    'ns_tt_btn_1': 0,
    'ns_tt_btn_2': 0,
    'ns_tt_btn_3': 0,
    'ns_tt_btn_4': 0,
    'ns_tt_btn_5': 0,
    'ns_tt_btn_6': 0,
    'ns_tb_btn_1': 0,
    'ns_tb_btn_2': 0,
    'ns_tb_btn_3': 0,
    'ns_tb_btn_4': 0,
    'ns_tb_btn_5': 0,
    'ns_tb_btn_6': 0,
    'ns_bt_btn_1': 0,
    'ns_bt_btn_2': 0,
    'ns_bt_btn_3': 0,
    'ns_bt_btn_4': 0,
    'ns_bt_btn_5': 0,
    'ns_bt_btn_6': 0,
    'ns_bb_btn_1': 0,
    'ns_bb_btn_2': 0,
    'ns_bb_btn_3': 0,
    'ns_bb_btn_4': 0,
    'ns_bb_btn_5': 0,
    'ns_bb_btn_6': 0,
    'west_top_btn_1': 0,
    'west_top_btn_2': 0,
    'west_bottom_btn_1': 0,
    'west_bottom_btn_2': 0,
}

disabledFan = {
    'east_top_btn_1': 0,
    'east_top_btn_2': 0,
    'east_bottom_btn_1': 0,
    'east_bottom_btn_2': 0,
    'ns_tt_btn_1': 0,
    'ns_tt_btn_2': 0,
    'ns_tt_btn_3': 0,
    'ns_tt_btn_4': 0,
    'ns_tt_btn_5': 0,
    'ns_tt_btn_6': 0,
    'ns_tb_btn_1': 0,
    'ns_tb_btn_2': 0,
    'ns_tb_btn_3': 0,
    'ns_tb_btn_4': 0,
    'ns_tb_btn_5': 0,
    'ns_tb_btn_6': 0,
    'ns_bt_btn_1': 0,
    'ns_bt_btn_2': 0,
    'ns_bt_btn_3': 0,
    'ns_bt_btn_4': 0,
    'ns_bt_btn_5': 0,
    'ns_bt_btn_6': 0,
    'ns_bb_btn_1': 0,
    'ns_bb_btn_2': 0,
    'ns_bb_btn_3': 0,
    'ns_bb_btn_4': 0,
    'ns_bb_btn_5': 0,
    'ns_bb_btn_6': 0,
    'west_top_btn_1': 0,
    'west_top_btn_2': 0,
    'west_bottom_btn_1': 0,
    'west_bottom_btn_2': 0,
}

boolBtnSelectedDuct = {
    'floor_1_btn_1': 0,
    'floor_1_btn_2': 0,
    'floor_1_btn_3': 0,
    'floor_1_btn_4': 0,
    'floor_1_btn_5': 0,
    'floor_1_btn_6': 0,
    'floor_2_btn_1': 0,
    'floor_2_btn_2': 0,
    'floor_2_btn_3': 0,
    'floor_2_btn_4': 0,
    'floor_2_btn_5': 0,
    'floor_2_btn_6': 0,
    'ceiling_1_btn_1': 0,
    'ceiling_1_btn_2': 0,
    'ceiling_1_btn_3': 0,
    'ceiling_1_btn_4': 0,
    'ceiling_1_btn_5': 0,
    'ceiling_1_btn_6': 0,
    'ceiling_2_btn_1': 0,
    'ceiling_2_btn_2': 0,
    'ceiling_2_btn_3': 0,
    'ceiling_2_btn_4': 0,
    'ceiling_2_btn_5': 0,
    'ceiling_2_btn_6': 0,
}

floorSegmentDesignation = {
    'floor_1_1': ['floor_1_btn_1', 'floor_1_btn_2', 'floor_1_btn_3'],
    'floor_1_2': ['floor_1_btn_4', 'floor_1_btn_5', 'floor_1_btn_6'],
    'floor_2_1': ['floor_2_btn_1', 'floor_2_btn_2', 'floor_2_btn_3'],
    'floor_2_2': ['floor_2_btn_4', 'floor_2_btn_5', 'floor_2_btn_6'],
    'ceiling_1_1': ['ceiling_1_btn_1', 'ceiling_1_btn_2', 'ceiling_1_btn_3'],
    'ceiling_1_2': ['ceiling_1_btn_4', 'ceiling_1_btn_5', 'ceiling_1_btn_6'],
    'ceiling_2_1': ['ceiling_2_btn_1', 'ceiling_2_btn_2', 'ceiling_2_btn_3'],
    'ceiling_2_2': ['ceiling_2_btn_4', 'ceiling_2_btn_5', 'ceiling_2_btn_6'],
}

boolBtnSelectedLight = {
    'light_1': 0,
    'light_2': 0,
    'light_3': 0,
    'light_4': 0,
    'light_5': 0,
    'light_6': 0,
    'light_7': 0,
    'light_8': 0,
    'light_9': 0, 
    'light_10': 0,
    'light_11': 0,
    'light_12': 0,
    'light_13': 0,
    'light_14': 0,
    'light_15': 0,
}

lightOverlayOpened = 0


def is_selected(pair):
    key, value = pair
    return value == 1

@login_required(login_url='loginPage')
def indexPage(request):
    context = {'boolBtnSelectedFan': boolBtnSelectedFan,
               'boolBtnSelectedDuct': boolBtnSelectedDuct,
               'boolBtnSelectedLight': boolBtnSelectedLight}
    # ,
    #            'lightOverlayOpened': lightOverlayOpened}
    
    fanPairs = {
        'ceiling_1': ['ns_tt_btn_1', 'ns_tt_btn_2', 'ns_tt_btn_3', 'ns_bt_btn_1', 'ns_bt_btn_2', 'ns_bt_btn_3'],
        'ceiling_2': ['ns_tt_btn_4', 'ns_tt_btn_5', 'ns_tt_btn_6', 'ns_bt_btn_4', 'ns_bt_btn_5', 'ns_bt_btn_6'],
        'floor_1': ['ns_tb_btn_1', 'ns_tb_btn_2', 'ns_tb_btn_3', 'ns_bb_btn_1', 'ns_bb_btn_2', 'ns_bb_btn_3'],
        'floor_2': ['ns_tb_btn_4', 'ns_tb_btn_5', 'ns_tb_btn_6', 'ns_bb_btn_4', 'ns_bb_btn_5', 'ns_bb_btn_6']
    }

    ductPositions = DuctPosition.objects.all()
    total = 0
    for key, value in fanPairs.items():
        identifiers = ['_btn_1', '_btn_2', '_btn_3', '_btn_4', '_btn_5', '_btn_6']
        for identifier in identifiers: 
            if ductPositions.filter(btnID=f'{key}{identifier}').exists():
                position = ductPositions.get(btnID=f'{key}{identifier}').position
                if position == 0:
                    total += 1
        if total == 6:
            for fan in value: 
                disabledFan[fan] = 1
                boolBtnSelectedFan[fan] = 0
        total = 0
    context['disabledFan'] = disabledFan
    print(disabledFan)

    # if request.method == 'GET': 
    #     print(f"Request GET: {request.GET}")
    #     boolBtnSelectedFan[request.GET['fanID']] = 1 - boolBtnSelectedFan[request.GET['fanID']]
        # boolBtnSelectedFan[request.GET['id']] = 1 - boolBtnSelectedFan[request.GET['id']]

    # if request.method == 'POST':
    #     boolBtnSelectedFan[request.POST['q']] = 1 - \
    #         boolBtnSelectedFan[request.POST['q']]
        
    lightModes = LightModes.objects.all()
    print(f"Light Modes: {lightModes.values()}")
    context['lightModes'] = list(LightModes.objects.all().values())

    return render(request, 'controller/index.html', context)

@login_required(login_url='loginPage')
def index(request, pk):
    if request.method == 'GET':
        boolBtnSelectedDuct[pk] = 1 - \
            boolBtnSelectedDuct[pk]

    return redirect(indexPage)

@login_required(login_url='loginPage')
def fanBtnUpdate(request):
    if request.method == 'GET':
        boolBtnSelectedFan[request.GET['fanID']] = 1 - boolBtnSelectedFan[request.GET['fanID']]

    return redirect('indexPage')

@login_required(login_url='loginPage')
def light(request, pk):
    if request.method == 'GET':
        boolBtnSelectedLight[pk] = 1 - boolBtnSelectedLight[pk]
        print(f"Light: {boolBtnSelectedLight}")

    return redirect(indexPage)

@login_required(login_url='loginPage')
def lightOverlayUpdate(request):
    if request.method == 'GET':
        global lightOverlayOpened
        lightOverlayOpened = 1 - lightOverlayOpened

    return redirect('indexPage')


def loginPage(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password=password)
            if user is not None:
                login(request, user)
                return redirect('indexPage')
    form = AuthenticationForm()
            
    return render(request, 'controller/login.html', {'form':form})

def logoutPage(request):
    logout(request)
    return redirect('loginPage')

def supplyCommand(request):
    selectedBtns = dict(filter(is_selected, boolBtnSelectedFan.items()))

    topic = 'command'
    client = paho.Client()
    client.connect(broker, port)
    command = json.dumps({'supply': selectedBtns})
    client.publish(topic, command)

    return redirect('indexPage')


def exhaustCommand(request):
    selectedBtns = dict(filter(is_selected, boolBtnSelectedFan.items()))

    topic = 'command'
    client = paho.Client()
    client.connect(broker, port)
    command = json.dumps({'exhaust': selectedBtns})
    client.publish(topic, command)

    return redirect('indexPage')


def offCommand(request):
    selectedBtns = dict(filter(is_selected, boolBtnSelectedFan.items()))

    topic = 'command'
    client = paho.Client()
    client.connect(broker, port)
    command = json.dumps({'off': selectedBtns})
    client.publish(topic, command)

    return redirect('indexPage')


def fanStatusCommand(request):
    selectedBtns = dict(filter(is_selected, boolBtnSelectedFan.items()))

    topic = 'command'
    client = paho.Client()
    client.connect(broker, port)
    command = json.dumps({'fanStatus': selectedBtns})
    client.publish(topic, command)

    return redirect('indexPage')

# def semiCloseCommand(request):  
#     selectedBtns = dict(filter(is_selected, boolBtnSelectedDuct.items()))

#     topic = 'command'
#     client = paho.Client()
#     client.connect(broker, port)
#     command = json.dumps({'semiClose': selectedBtns})
#     client.publish(topic, command)

#     return redirect('indexPage')

def semiCloseCommand(request):
    if request.method == 'GET':
        selectedBtns = dict(filter(is_selected, boolBtnSelectedDuct.items()))
        print(f"Selected Duct Buttons: {selectedBtns}")
        for selectedBtn in selectedBtns.keys():
            topic = 'command'
            client = paho.Client()  
            client.connect(broker, port)
            command = json.dumps({'semiOpen': {selectedBtn: request.GET['position']}})
            client.publish(topic, command)
            time.sleep(2)
    return redirect('indexPage')  

# def semiOpenCommand(request):
#     selectedBtns = dict(filter(is_selected, boolBtnSelectedDuct.items()))

#     topic = 'command'
#     client = paho.Client()
#     client.connect(broker, port)
#     command = json.dumps({'semiOpen': selectedBtns})
#     client.publish(topic, command)

#     return redirect('indexPage')


def semiOpenCommand(request): 
    if request.method == 'GET':
        topic = 'command'
        client = paho.Client()  
        client.connect(broker, port)
        command = json.dumps({'semiOpen': {request.GET['duct']: request.GET['position']}})
        client.publish(topic, command)
        return redirect('indexPage')    

def openCommand(request):
    selectedBtns = dict(filter(is_selected, boolBtnSelectedDuct.items()))

    topic = 'command'
    client = paho.Client()
    client.connect(broker, port)
    command = json.dumps({'open': selectedBtns})
    client.publish(topic, command)

    return redirect('indexPage')


def closeCommand(request):
    selectedBtns = dict(filter(is_selected, boolBtnSelectedDuct.items()))

    topic = 'command'
    client = paho.Client()
    client.connect(broker, port)
    command = json.dumps({'close': selectedBtns})
    client.publish(topic, command)

    return redirect('indexPage')


def ductStatusCommand(request):
    selectedBtns = dict(filter(is_selected, boolBtnSelectedDuct.items()))

    topic = 'command'
    client = paho.Client()
    client.connect(broker, port)
    command = json.dumps({'ductStatus': selectedBtns})
    client.publish(topic, command)

    return redirect('indexPage')

@login_required(login_url='loginPage')
def executeLightCommand(request):
    if request.method == 'GET':
        selectedBtns = dict(filter(is_selected, boolBtnSelectedLight.items()))
        commandDict = {}
        for key in selectedBtns.keys():
            commandDict[key] = {'x': request.GET['x'], 'y': request.GET['y'], 'on': request.GET['on'], 'brightness': request.GET['brightness']}
            print(commandDict)

        topic = 'command'
        client = paho.Client()
        client.connect(broker, port)
        command = json.dumps({'light': commandDict})
        print(f"Light command: {command}")
        client.publish(topic, command)

    return redirect('indexPage')

@login_required(login_url='loginPage')
def saveLights(request):
    selectedBtns = dict(filter(is_selected, boolBtnSelectedLight.items()))
    saveStr = '' 
    print(f"Selected Light Buttons: {selectedBtns}")
    for key, value in selectedBtns.items(): 
        saveStr += f"{key}:"
    saveStr = saveStr[:-1]
    print(f"Color: {request.GET.get('color')}")
    lightModes = LightModes(mode_name=request.GET.get('modeName'),
                            on_lights=saveStr,
                            color=request.GET.get('color'),
                            brightness=request.GET.get('brightness'))
    lightModes.save()


    return redirect('indexPage')

def fans(request):
    print(FanButtonModel.objects.all())
    return JsonResponse(list(FanButtonModel.objects.all().values()), safe=False)


def ducts(request):
    return JsonResponse(list(DuctButtonModel.objects.all().values()), safe=False)

def multipleSelectFunc(ductName):
    # if ductName in boolBtnSelectedDuct.keys():
    for item in floorSegmentDesignation[ductName]:
        boolBtnSelectedDuct[item] = 1 - boolBtnSelectedDuct[item]
    # elif ductName in boolBtnSelectedFan.keys():
    #     boolBtnSelectedFan[ductName] = 1 - boolBtnSelectedFan[ductName]


def multipleSelect(request):
    if request.method == "POST":
        print(f'==> {request.POST["q"]}')

        multipleSelectFunc(request.POST['q'])

    return redirect('indexPage')

def createMode(request):
    mode = Mode()
    mode.save()
    return JsonResponse({'mode_id': mode.mode_id})

def addMode(request):
    # if request.method == 'GET':
    #     mode = Mode(mode_name=request.GET.get('modeName'),
    #                 mode_description=request.GET.get('modeDescription'))
        
    #     mode.save()
    #     modeObject = Mode.objects.get(mode_id=mode.mode_id)

    #     for (key, value) in boolBtnSelectedFan.items():
    #         if value == 1:
    #             modeElement = ModeElements(mode_id=modeObject, mode_identifier=key, mode_type='fan')
    #             modeElement.save()
    #     for (key, value) in boolBtnSelectedDuct.items():
    #         if value == 1:
    #             modeElement = ModeElements(mode_id=modeObject, mode_identifier=key, mode_type='duct')
    #             modeElement.save()  
    
    if request.method == 'GET': 
        modeObject = Mode.objects.get(mode_id=request.GET.get('modeID'))
        if request.GET.get('mode') == 'fan':
            modeElement = ModeElements(mode_id=modeObject, 
                                       mode_identifier=request.GET.get('fanButton'),
                                       mode_command=request.GET.get('fanControl'),
                                       mode_type='fan')
            modeElement.save()
        elif request.GET.get('mode') == 'duct':
            modeElement = ModeElements(mode_id=modeObject, 
                                       mode_identifier=request.GET.get('ductButton'),   
                                       mode_command=request.GET.get('ductControl'),
                                       mode_type='duct')
            modeElement.save()
    return JsonResponse({'status': 'success'})

def getModes(request):
    return JsonResponse(list(Mode.objects.all() .values()), safe=False)  
    
def executeMode(request):
    if request.method == 'GET':
        modeObject = Mode.objects.get(mode_id=request.GET.get('modeID'))
        modeElements = ModeElements.objects.filter(mode_id=modeObject)
        print(modeObject)
        print(modeElements)


        #json.dumps(modeElements)
        #json.dumps(modeElements)

        for modeElement in modeElements:
            topic = 'command'
            client = paho.Client()
            client.connect(broker, port)
            command = json.dumps({modeElement.mode_command: {modeElement.mode_identifier: 1}})
            print(f"Command: {command}")
            client.publish(topic, command)
            time.sleep(10)
            
    return JsonResponse({'status': 'success'})

def deleteMode(request):
    if request.method == 'GET':
        modeObject = Mode.objects.get(mode_id=request.GET.get('modeID'))
        modeObject.delete()
    return JsonResponse({'status': 'success'})   

def ductsPosition(request):
    if request.method == 'GET':
        position = DuctPosition.objects.get(btnID=request.GET.get('btnID')).position
        print(f'position: {position}')
    
    # return JsonResponse({'position': position})
    return HttpResponse(position)
    

def ductPositionUpdate(request):
    if request.method == 'GET':
        ductObject = DuctPosition.objects.get(btnID=request.GET.get('btnID'))
        ductObject.position = request.GET.get('position')
        ductObject.save()
        
    return JsonResponse({'status': 'success'})

def sensorDataEntry(request):
    # if request.method == 'GET':
        # print("===?" + str(request.GET.get('temperature').lstrip().split(' ')[0]))
        #Time Stamp, Status, Altitude, Temperature,Humidity,Pressure, Air Speed, eCO2, TVOC, AQI, Dust Sensor, Light Sensor
        #print(f"{datetime.datetime.now()} {request.GET.get('status')} {request.GET.get('altitude')} {request.GET.get('temperature')} {request.GET.get('humidity')} {request.GET.get('pressure')} {request.GET.get('windSpeed')} {request.GET.get('eco2')} {request.GET.get('tvoc')} {request.GET.get('aqi')} {request.GET.get('dustDensity')} {request.GET.get('lux')}
        
        # sensorData = SensorData(timestamp=datetime.datetime.now(),
        #                         temperature=request.GET.get('temperature').lstrip().split(' ')[0],
        #                         humidity=request.GET.get('humidity').lstrip().split(' ')[0],
        #                         pressure=request.GET.get('pressure').lstrip().split(' ')[0],
        #                         altitude=request.GET.get('altitude').lstrip().split(' ')[0],
        #                         lux=request.GET.get('lux').lstrip().split(' ')[0],
        #                         dustDensity=request.GET.get('dustDensity').lstrip().split(' ')[0],
        #                         windSpeed=request.GET.get('windSpeed').lstrip().split(' ')[0] if request.GET.get('windSpeed')!="nan" else 0,
        #                         status=request.GET.get('status').lstrip(),
        #                         aqi=request.GET.get('aqi').lstrip(),
        #                         tvoc=request.GET.get('tvoc').lstrip().split(' ')[0],
        #                         eco2=request.GET.get('eco2').lstrip().split(' ')[0])

        # sensorData = SensorData(timestamp=datetime.datetime.now(),
        #                         temperature=request.GET.get('temperature'),
        #                         humidity=request.GET.get('humidity'),
        #                         pressure=request.GET.get('pressure'),
        #                         altitude=request.GET.get('altitude'),
        #                         lux=request.GET.get('lux'),
        #                         dustDensity=request.GET.get('dustDensity'),
        #                         windSpeed=request.GET.get('windSpeed') if request.GET.get('windSpeed')!="nan" else 0,
        #                         status=request.GET.get('status'),
        #                         aqi=request.GET.get('aqi'),
        #                         tvoc=request.GET.get('tvoc'),
        #                         eco2=request.GET.get('eco2'))

        # sensorData.save()
        
    return JsonResponse({'status': 'success'})

def getDuctMaxValue(request):   
    if request.method == 'GET':
        max_value_instance = DuctMaxValue.objects.first()
        if max_value_instance:
            max_value = max_value_instance.max_value
        else:
            max_value = None  # or set a default value
    return JsonResponse({'ductMaxValue': max_value})


def export_sensor_data(request):
    return render(request, 'controller/export.html')    

def export_csv(model, model_name):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{model_name}.csv"'

    writer = csv.writer(response)
    fields = [field.name for field in model._meta.fields]
    writer.writerow(fields)

    for instance in model.objects.all():
        row = [getattr(instance, field) for field in fields]
        writer.writerow(row)

    return response

def export_sensor_data1_csv(request):
    return export_csv(SensorData1, 'SensorData1')

def export_sensor_data2_csv(request):
    return export_csv(SensorData2, 'SensorData2')

def export_sensor_data3_csv(request):
    return export_csv(SensorData3, 'SensorData3')

def export_sensor_data4_csv(request):
    return export_csv(SensorData4, 'SensorData4')

def export_sensor_data5_csv(request):
    return export_csv(SensorData5, 'SensorData5')

def export_sensor_data6_csv(request):
    return export_csv(SensorData6, 'SensorData6')
    


def power_sensor(request):
    if request.method == 'GET':
        data = request.GET.get('data')

        topic = data.split(':')[0]
        command = data.split(":")[1]
        client = paho.Client() 
        client.connect(broker, port)
        client.publish(topic, command)

    return redirect('indexPage')


def power_pi(request): 
    if request.method == 'GET': 
        data = request.GET.get('data')

        topic = data.split(':')[0]
        command = data.split(":")[1]
        client = paho.Client() 
        client.connect(broker, port)
        client.publish(topic, command)

    return redirect('indexPage')

def power_duct(request): 
    if request.method == 'GET': 
        data = request.GET.get('data')

        topic = data.split(':')[0]
        command = data.split(":")[1]
        client = paho.Client() 
        client.connect(broker, port)
        client.publish(topic, command)

    return redirect('indexPage')


def setOffset(request):
    if request.method == 'GET': 
        offset = request.GET.get('offset')
        offset_instance = Co2Offset.objects.first()
        if offset_instance:
            offset_instance.offset = offset
            offset_instance.save()
        else:
            offset_instance = Co2Offset(offset=offset)
            offset_instance.save()
        