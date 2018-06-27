# -*- coding: utf-8 -*-


#pyaudio：利用pyaudio从电脑端录制音频保存到指定文件夹+将录音上传到服务器+进行识别
import wave
from pyaudio import PyAudio,paInt16
import json
import base64
import os
import requests
import time


RATE = "16000"
FORMAT = "wav"
CUID="wate_play"
DEV_PID="1536"

framerate=16000
NUM_SAMPLES=2000
channels=1
sampwidth=2
TIME=2

def get_token():
    server = "https://openapi.baidu.com/oauth/2.0/token?"
    grant_type = "client_credentials"
    #API Key
    client_id = "qRHV7hrxj8vtAGuZOpG0zW58"
    #Secret Key
    client_secret = "Bg3Bmx3uPeCUnvuHxnS16HLnNiVPuPnz" 

    #拼url
    url ="%sgrant_type=%s&client_id=%s&client_secret=%s"%(server,grant_type,client_id,client_secret)
    #获取token
    res = requests.post(url)
    token = json.loads(res.text)["access_token"]
    print('get_token调用函数成功！'+token)
    return token

def get_word(token):
    with open(audio_file, "rb") as f:
        speech = base64.b64encode(f.read()).decode('utf8')
    size = os.path.getsize(audio_file)
    headers = { 'Content-Type' : 'application/json'} 
    url = "https://vop.baidu.com/server_api"
    data={
            "format":FORMAT,
            "rate":RATE,
            "dev_pid":DEV_PID,
            "speech":speech,
            "cuid":CUID,
            "len":size,
            "channel":1,
            "token":token,
        }
    req = requests.post(url,json.dumps(data),headers)
    result = json.loads(req.text)
    print(result)
    ret0=result["result"][0]
    print(ret0)
    return result

def save_wave_file(filename,data):
    '''save the date to the wavfile'''
    wf=wave.open(filename,'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(sampwidth)
    wf.setframerate(framerate)
    wf.writeframes(b"".join(data))
    wf.close()

def my_record():
    pa=PyAudio()
    stream=pa.open(format = paInt16,channels=1,
                   rate=framerate,input=True,
                   frames_per_buffer=NUM_SAMPLES)
    my_buf=[]
    count=0
    print('.')
    while count<TIME*10:#控制录音时间
        string_audio_data = stream.read(NUM_SAMPLES)
        my_buf.append(string_audio_data)
        count+=1

    save_wave_file('out.wav',my_buf)
    stream.close()


chunk=2014
def play():
    wf=wave.open(r"out.wav",'rb')
    p=PyAudio()
    stream=p.open(format=p.get_format_from_width(wf.getsampwidth()),channels=
    wf.getnchannels(),rate=wf.getframerate(),output=True)
    while True:
        data=wf.readframes(chunk)
        if data=="":break
        stream.write(data)
    stream.close()
    p.terminate()

if __name__ == '__main__':
#     my_record()
    audio_file='16k.wav'
    token=get_token()
    ret = get_word(token)
