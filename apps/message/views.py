from django.shortcuts import render
from apps.message.models import UserMessage
import random

import datetime

'''
获取提交表单，填入提交信息并存储到数据库中
'''
def submitform(request):
    return render(request,'message_form.html')
'''
显示提交板信息
'''
def showform(request):
    # 上传到数据库
    if request.method == 'POST':
        usermessage = UserMessage()
        usermessage.name = request.POST.get('name','')
        usermessage.time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        usermessage.address = request.POST.get('address','')
        usermessage.message = request.POST.get('message','')
        usermessage.object_id = str(random.randint(0,10000)).zfill(5) # 自动补零
        usermessage.save()
    # 取出当前数据库中所有记录，并传入到下一个html中
    all_messages = UserMessage.objects.all().order_by('time')
    for message in all_messages:
        message.time = datetime.datetime.strftime(message.time,'%Y-%m-%d %H:%M:%S')

    return render(request,'message_board.html', {
        'all_messages':all_messages,
    })