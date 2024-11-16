# importing the requests library
import requests

# api-endpoint
URL = "https://projekte.kvv-efa.de/mangangtrias/trias"

with open('kvv.xml', 'r') as file:
    mydata = file.read()


# sending get request and saving the response as response object
r = requests.get(url = URL, data = mydata)

print(r)


