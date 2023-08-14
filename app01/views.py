# Create your views here.
# -*- coding: utf-8 -*-
from django.shortcuts import HttpResponse
from utils.tencent.sms import send_sms_single
import random

def send_sms(request):
    code = random.randrange(10000,99999)
    time = 1
    res = send_sms_single('15733160817', 1896751, [code,time])
    print(res)
    return HttpResponse('短信发送成功')