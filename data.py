# importing the requests library
import requests
import xmltodict, json
import xml.etree.ElementTree as ET
import json

# api-endpoint
URL = "https://projekte.kvv-efa.de/mangangtrias/trias"

with open('kvv.xml', 'r') as file:
     mydata = file.read()


# sending get request and saving the response as response object

headers = {'Content-Type': 'application/xml'} # set what your server accepts
answer = requests.post(url= URL, data=mydata, headers=headers).text
#print(answer)

#with open ('data.xml','w') as data:
#    data.write(answer) 

root = ET.fromstring(answer) 



#print(root)
dat = root.attrib
#print(dat)

input_ = json.dumps(answer)

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

Trias = trias_data_reimport["Trias"]
ServiceDelivery = Trias["ServiceDelivery"]
DeliveryPayload = ServiceDelivery["DeliveryPayload"]
TripResponse = DeliveryPayload["TripResponse"]
TripResult = TripResponse["TripResult"]
for i in TripResult:
    Trip_name = i["Trip"]["TripLeg"]["TimedLeg"]["Service"]["PublishedLineName"]["Text"]
    text_line = Trip_name.encode('latin1').decode('utf8')
    print(text_line)

for f in TripResult:
    Trip_time = f["Trip"]["TripLeg"]["TimedLeg"]["LegBoard"]["ServiceDeparture"]["TimetabledTime"]
    text_time = Trip_time.encode('latin1').decode('utf8')
    print(text_time)
    
    






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