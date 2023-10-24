from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import FanButtonModel, DuctButtonModel
from django.contrib.auth.models import User
from .forms import UserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
import paho.mqtt.client as paho
import json

broker = '146.190.138.255'
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


def is_selected(pair):
    key, value = pair
    return value == 1

@login_required(login_url='loginPage')
def indexPage(request):
    context = {'boolBtnSelectedFan': boolBtnSelectedFan,
               'boolBtnSelectedDuct': boolBtnSelectedDuct}

    if request.method == 'POST':
        boolBtnSelectedFan[request.POST['q']] = 1 - \
            boolBtnSelectedFan[request.POST['q']]

    return render(request, 'controller/index.html', context)

@login_required(login_url='loginPage')
def index(request, pk):
    if request.method == 'GET':
        boolBtnSelectedDuct[pk] = 1 - \
            boolBtnSelectedDuct[pk]

    return redirect(indexPage)

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


def semiOpenCommand(request):
    selectedBtns = dict(filter(is_selected, boolBtnSelectedDuct.items()))

    topic = 'command'
    client = paho.Client()
    client.connect(broker, port)
    command = json.dumps({'semiOpen': selectedBtns})
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
