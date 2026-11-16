
import requests

url = "https://api.chucknorris.io/jokes/random"

vastaus = requests.get(url)
tiedot = vastaus.json()

print(tiedot["value"])
