import urllib.request
import xml.etree.ElementTree as ET

url=input('Enter Location: ')
xml = urllib.request.urlopen(url).read()

print('Retrieving:', url)
print('Retrieved', len(xml),'characters')

stuff = ET.fromstring(xml)
lst = stuff.findall('.//count')

print('Count:', len(lst))
sum=0
for item in lst:
    sum+=int(item.text)
print('Sum:', sum)
