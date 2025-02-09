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

o = xmltodict.parse(data_trias)

print(o)
with open('trias.json', 'w') as f:
     json.dump(o,f)
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