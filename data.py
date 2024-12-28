# importing the requests library
import requests
import xml.etree.ElementTree as ET

# api-endpoint
URL = "https://projekte.kvv-efa.de/mangangtrias/trias"

with open('kvv.xml', 'r') as file:
     mydata = file.read()


# sending get request and saving the response as response object

headers = {'Content-Type': 'application/xml'} # set what your server accepts
answer = requests.post(url= URL, data=mydata, headers=headers).text
print(answer)

#with open ('data.xml','w') as data:
#    data.write(answer) 

root = ET.fromstring(answer) 



print(answer)
#dat = root.attrib
#print(dat)

data_ncorrected = answer.replace('/n','')
#data_correct = data_ncorrected.replace()

with open('trial_data.xml', 'w', encoding="utf-8") as f:
     f.write(data_ncorrected)




#T3x9Kzw3v6C5