from urllib.request import urlopen
import json
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

info = json.loads(data)

sum = 0
for item in info['comments']:
    sum += item['count']
print(f"Sum: {sum}")

