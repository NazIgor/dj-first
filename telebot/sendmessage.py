import requests
from .models import TeleSettings

def sendTelega(tg_name, tg_phone):
    settings= TeleSettings.objects.get(pk=1)
    token=str(settings.tg_token)
    chat_id=str(settings.tg_chat)
    text=str(settings.tg_txt)

    a=text.find('{')
    b=text.find('}')
    c=text.rfind('{')
    d=text.rfind('}')

    part_1=text[0:a]
    part_2=text[b+1:c]
    part_3=text[d:-1]

    text_slice=part_1+tg_name+part_2+tg_phone+part_3

    api="https://api.telegram.org/bot"
    urlMessage=api+token+'/sendMessage'
    req=None

    try:
        req=requests.post(urlMessage, data={'chat_id':chat_id, 'text':text_slice})
    except Exception as e:
        print (e)

