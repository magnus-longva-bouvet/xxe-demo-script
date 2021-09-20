import requests

with open("normal_use.xml", "r") as f:
    data = f.read()


r = requests.post("https://kaketyv.no/hello", headers={'Content-Type': "application/xml"}, data=data)

print(r.text)