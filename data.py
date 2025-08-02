import requests
import xmltodict, json
import xml.etree.ElementTree as ET
import json
import time

# api-endpoint
URL = "https://projekte.kvv-efa.de/mangangtrias/trias"


time_now = time.strftime("%Y-%m-%dT%H:%M:%S")  
time_now_edited = time_now.replace("T", "")
time_now_clean = time_now_edited.replace("Z", "")
time_fuck_you = time_now_clean.replace("-", "")
time_a = time_fuck_you.replace(":", "")
time_point_a = int(time_a)
print(time_a)

print(time_now)

with open('kvv.xml', 'r') as file:
     mydata = file.read()

data_modified = mydata.replace('2025-03-02T17:36:00',time_now)
# sending get request and saving the response as response object

headers = {'Content-Type': 'application/xml'} # set what your server accepts
answer = requests.post(url= URL, data=data_modified, headers=headers).text
print(answer)

#with open ('data.xml','w') as data:
#    data.write(answer) 

root = ET.fromstring(answer) 



#print(root)
dat = root.attrib
#print(dat)

input_ = json.dumps(answer)

text_trias =[]

inputfix1 = input_.replace("\\n","")
inputfix2= inputfix1.replace('"', '', 1)
inputfix3 = inputfix2.replace('>"','>', 1)
inputfix4 = inputfix3.replace('\\"','"')

data_trias = inputfix4

trias_dict = xmltodict.parse(data_trias)

#print(o)
with open('trias.json', 'w', encoding="utf-8") as trias_json:
     json.dump(trias_dict,trias_json)

with open('trias.json', 'r', encoding="unicode-escape") as trias_json_load:
    trias_data_reimport = json.load(trias_json_load)

Trias = trias_data_reimport["Trias"]["ServiceDelivery"]["DeliveryPayload"]["TripResponse"]["TripResult"]
ServiceDelivery = Trias
DeliveryPayload = ServiceDelivery
TripResponse = DeliveryPayload
TripResult = TripResponse
for i in TripResult:
    Trip_name = i["Trip"]["TripLeg"][0]["TimedLeg"]["Service"]["PublishedLineName"]["Text"]
    text_line = Trip_name.encode('latin1').decode('utf8')
    #print(text_line)

    Trip_time = i["Trip"]["TripLeg"][0]["TimedLeg"]["LegBoard"]["ServiceDeparture"]["TimetabledTime"]
    text_time = Trip_time.encode('latin1').decode('utf8')
    time_edit = text_time.replace("T","")
    time_edit_final = time_edit.replace("Z","")
    time_dep = time_edit_final.replace("-", "")
    time_b = time_dep.replace(":", "")
    time_point_b = int(time_b)
    time_departure = time_point_b-time_point_a
    print(time_departure)
    
    Trip_dest= i["Trip"]["TripLeg"][0 ]["TimedLeg"]["Service"]["DestinationText"]["Text"]	
    text_dest = Trip_dest.encode('latin1').decode('utf8')
    


    #trias_result = "Linie:" + " "+ text_line + " " +"Nach"+ " "+ text_dest + " " +"Ankunft" + " "+ time_departure

    #text_trias.extend([trias_result])
        

    #with open('result.txt', 'w') as result:
       # result.write(text_trias)


    #print(trias_result)
    






    



 





#with open('data.xml', 'w') as data:
    # data.write(data_trias)


#with open('data.xml',mode="r", encoding="utf-8") as data_u:
    #data_usable = data_u.read()

#print(data_usable)

root_ = ET.fromstring(data_trias)





#for country in root_.findall('Service'):
   # rank = country.find('PublishedLineName').text
  #  name = country.get('DestinationText')
   # print(name, rank)


#T3x9Kzw3v6C5

print("Request done")
