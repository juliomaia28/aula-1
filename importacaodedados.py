import requests

url = "https://www.sofascore.com/team/football/vasco/1974"
response = requests.get(url)
data = response.text
print(data)