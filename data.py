import requests
import xmltodict, json
import xml.etree.ElementTree as ET
import json
import time

# api-endpoint
URL = "https://projekte.kvv-efa.de/mangangtrias/trias"

time_now = time.strftime("%Y-%m-%dT%H:%M:%S")  

print(time_now)

with open('kvv.xml', 'r') as file:
     mydata = file.read()

data_modified = mydata.replace('2025-03-02T17:36:00',time_now)
# sending get request and saving the response as response object

headers = {'Content-Type': 'application/xml'} # set what your server accepts
answer = requests.post(url= URL, data=data_modified, headers=headers).text
#print(answer)

#with open ('data.xml','w') as data:
#    data.write(answer) 


input_ = json.dumps(answer)


inputfix1 = input_.replace("\\n","")
inputfix2= inputfix1.replace('"', '', 1)
inputfix3 = inputfix2.replace('>"','>', 1)
data_trias = inputfix3.replace('\\"','"')


trias_dict = xmltodict.parse(data_trias)

with open('test.json','w') as a:
	json.dump(trias_dict, a)

exit()

TripResult = trias_dict["Trias"]["ServiceDelivery"]["DeliveryPayload"]["TripResponse"]["TripResult"]




with open('trias.json', 'w', encoding="utf-8") as trias_json:
     json.dump(TripResult, trias_json)

with open('trias.json', 'r', encoding="unicode-escape") as trias_json_load:
    trias_data_reimport = json.load(trias_json_load)


trip = trias_data_reimport["Trip"]["TripLeg"]

with open('debug.json', 'w') as e:
    json.dump(trip, e)

    
for i in trip :

    Trip_name = i["TimedLeg"]["Service"]["PublishedLineName"]["Text"]
    text_line = Trip_name.encode('latin1').decode('utf8')

    Trip_time = i["TimedLeg"]["LegAlight"]["ServiceArrival"]["TimetabledTime"]
    text_time = Trip_time.encode('latin1').decode('utf8')
        
    Trip_dest = i["TimedLeg"]["LegAlight"]["StopPointName"]["Text"]
    text_dest = Trip_dest.encode('latin1').decode('utf8')
    
    trias_result = "Linie:" + " "+ text_line + " " +"Nach"+ " "+ text_dest + " " +"Ankunft" + " "+ text_time 

    print(trias_result)
    

print("Request done")
