import requests

#Provided when you generate a SAS Token in Azure
blobUrl = ""

#Prompt user for ip address
ipAddress = input('Enter IP that you would like to block here: ')

#Adds block type "&comp=appendblock" and new line with IP address
putRequest = requests.put(blobUrl + "&comp=appendblock", data = "\n" + ipAddress)

getRequest = requests.get(blobUrl)

print(putRequest.text)

print(getRequest.text)
