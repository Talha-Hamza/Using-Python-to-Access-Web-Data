import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

count = input("Enter count: ")
position = input("Enter position: ")
url = input('Enter URL - ')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
count = int(count)
count = count + 1
for i in range(count):
    print("Retrieving: ", url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    
    # Retrieve all of the anchor tags
    tags = soup('a')
    
    j = 0
    
    for tag in tags:
        j = j + 1
        # print(tag.get('href', None))
        if j == int(position):
            url = tag.get('href', None)
            break
        