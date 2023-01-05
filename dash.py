import requests
import streamlit as st
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.5",
}
http_proxy = "http://0.0.0.0.0:0000"
proxies = {
    "http": http_proxy,
}
for url in ['https://w3schools.com','https://www.google.it','https://it.bidoo.com/auction.php?a=Protein_Muesli_Cioccolato_30453593']:
  x = requests.get(url,verify=False,headers=headers,proxies=proxies)
  st.write(f"{url}: {x.status_code}")

