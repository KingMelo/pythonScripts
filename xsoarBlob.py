import requests

#Provided when you generate a SAS Token in Azure
blobUrl = "https://hobgoblin.blob.core.windows.net/edl/edllist.txt?sp=racwd&st=2022-09-15T17:39:38Z&se=2023-09-16T01:39:38Z&spr=https&sv=2021-06-08&sr=b&sig=zKc2ITY7hDAFRTj09cYLaWXCphgkE%2FeM0FYbICRLCj8%3D"

#Prompt user for ip address
ipAddress = input('Enter IP that you would like to block here: ')

#Adds block type "&comp=appendblock" and new line with IP address
putRequest = requests.put(blobUrl + "&comp=appendblock", data = "\n" + ipAddress)

getRequest = requests.get(blobUrl)

print(putRequest.text)

print(getRequest.text)