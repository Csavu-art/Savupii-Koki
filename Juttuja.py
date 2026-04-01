import requests
import json

hakusana = input("Anna hakusana: ")
try:
# Pyynnön malli: https://api.tvmaze.com/search/shows?q=girls
    pyyntö = "https://api.tvmaze.com/search/shows?q=" + hakusana
    vastaus = requests.get(pyyntö).json()
    for a in vastaus:
        print(a["show"]["name"])
except requests.exceptions.RequestException as e:
    print ("Hakua ei voitu suorittaa." + e)