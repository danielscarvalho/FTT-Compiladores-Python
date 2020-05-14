# pip install requests
# 

import requests

#print(requests.get("https://en.wikipedia.org/wiki/Infrastructure").content)
print(requests.get("https://en.wikipedia.org/wiki/Infrastructure").text)