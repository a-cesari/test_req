import requests
for url in [''https://w3schools.com','https://www.google.it']:
  x = requests.get(url,verify=False,headers={'User-Agent' : "Magic Browser"})
  print(f"{url}: {x.status_code}")

