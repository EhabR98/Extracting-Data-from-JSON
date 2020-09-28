import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import json
sum=0

url = input('Enter location: ')
print('Retrieving', url)

data=urllib.request.urlopen(url).read()
print('Retrieved',len(str(data)),'character')

info = json.loads(data)
counts= info['comments']

for count in range(len(counts)):
    sum= sum+int(counts[count]['count'])
print(sum)
