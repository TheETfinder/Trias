# importing the requests library
import requests

# api-endpoint
URL = "https://projekte.kvv-efa.de/mangangtrias/trias"

with open('kvv.xml', 'r') as file:
    kvvdata = file.read()


# sending get request and saving the response as response object
r = requests.get(url = URL, data= kvvdata)

print(r)


#F76VP9vhNQa7

