import requests
import streamlit as st
for url in ['https://w3schools.com','https://www.google.it']:
  x = requests.get(url,verify=False,headers={'User-Agent' : "Magic Browser"})
  st.write(f"{url}: {x.status_code}")

