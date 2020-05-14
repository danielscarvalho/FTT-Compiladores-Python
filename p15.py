# pip install requests
# 

import requests

#print(requests.get("https://api.duckduckgo.com/?q=Sonia+Braga&format=json&pretty=0").text)
#print(requests.get("https://api.duckduckgo.com/?q=Sonia+Braga&format=json&pretty=1").text)
#print(requests.get("https://api.duckduckgo.com/?q=Sonia+Braga&format=xml&pretty=1").text)


data = requests.get("https://api.duckduckgo.com/?q=Sonia+Braga&format=json&pretty=1").json()

print(data.keys())
print()
print(data["Abstract"])
print()

for d in data["RelatedTopics"]:
    print(d)