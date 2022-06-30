import re
import json
import requests
from geopy.distance import geodesic

header={"User-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 YaBrowser/22.5.3.680 Yowser/2.5 Safari/537.36"}
a=json.loads(requests.get("https://ipinfo.io/2.16.53.0/json").text)
b=json.loads(requests.get("https://ipinfo.io/178.141.120.90/json").text)
print(a,b)
print(geodesic(b["loc"],a["loc"]).km)

