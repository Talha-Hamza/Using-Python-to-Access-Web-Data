from urllib.request import urlopen
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
print(f"Retrieving: {url}")
data = urlopen(url, context=ctx).read()
print(f"Retrieved {len(data)} characters")
# print(data.decode())

tree = ET.fromstring(data)

commentinfo = tree.findall('comments/comment')
# print(len(commentinfo))
list = []
for item in commentinfo:
    # print('Count: ', item.find('count').text)
    list.append(int(item.find('count').text))

print(f"My sum:  {sum(list)}")

