import requests
import xmltodict, json
import xml.etree.ElementTree as ET
import json
import time
from datetime import datetime

# api-endpoint
URL = "https://projekte.kvv-efa.de/mangangtrias/trias"

time_now = time.strftime("%Y-%m-%dT%H:%M:%S")
day = time.strftime("%Y-%m-%dT")

time_fix = time_now.replace("T", "")
time = time_fix.replace("Z", "")

print(time_now)

with open('kvv.xml', 'r') as file:
     mydata = file.read()

data_modified = mydata.replace('timenow',time_now)

headers = {'Content-Type': 'application/xml'} # set what your server accepts
answer = requests.post(url= URL, data=data_modified, headers=headers).text

data = json.dumps(xmltodict.parse(answer))

fix = data.replace('trias:','')

with open('test.json','w') as a:
	a.write(fix)

with open('test.json','r') as l:
	tri = json.load(l)

trias = tri["Trias"]

StopEventResult = trias["ServiceDelivery"]["DeliveryPayload"]["StopEventResponse"]["StopEventResult"]

with open('trias.json', 'w', encoding="utf-8") as trias_json:
     json.dump(StopEventResult, trias_json)

with open('trias.json', 'r', encoding="unicode-escape") as trias_json_load:
    trip = json.load(trias_json_load)


for i in trip :

    Trip_name = i["StopEvent"]["Service"]["ServiceSection"]["PublishedLineName"]["Text"]
    text_line = Trip_name.encode('latin1').decode('utf8')

    Trip_time = i["StopEvent"]["ThisCall"]["CallAtStop"]["ServiceDeparture"]["TimetabledTime"]
    text_time = Trip_time.encode('latin1').decode('utf8')

    Trip_dest = i["StopEvent"]["Service"]["DestinationText"]["Text"]
    text_dest = Trip_dest.encode('latin1').decode('utf8')

    trias_time = text_time.replace("Z","")
    arr_time = trias_time.replace("T", "")
    arr = text_time.replace(day, "")
    time_arr = arr.replace("Z", "")
    print(arr_time)
#    dt = datetime.strptime(arr_time, "%a, %d %b %Y %H:%M:%S")
#    datetime = datetime.datetime-strptime(time,"%Y-%m-%d%H:%M:%S")

#    print(dt)
#    print(datetime)

    trias_result = "Linie:" + " "+ text_line + " " +"Nach"+ " "+ text_dest + " " +"Abfahrt:" + " "+ time_arr

    print(trias_result)

print(type(text_time))
print("Request done")
