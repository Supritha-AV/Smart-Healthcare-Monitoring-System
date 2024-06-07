import requests
data=requests.get("https://api.thingspeak.com/channels/2054287/feeds.json?api_key=W1GRZLGWAC3ZWWTU&results=2")
print(data)
hb=int(data.json()['feeds'][-1]['field1'])
ecg=int(data.json()['feeds'][-1]['field3'])
print(hb)
print(ecg)
if ecg<300:
    ec=0
elif ecg>300 and ecg <400:
    ec=1
else:
    ec=2
print(ec)
