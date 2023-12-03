import requests,json

apikey ="163b2810f5b4cce441199e6e339222b3"

baseurl="https://api.openweathermap.org/data/2.5/weather?q="
city=input("Enter your City : ")
print(city)
curl=baseurl+city+"&appid="+apikey

response=requests.get(curl)

data =  response.json()
print("Current Temperature : ",data["main"]["temp"])
print("Current Temperature feels like : ",data["main"]["feels_like"])
print("Maximum Temperature : ",data["main"]["temp_max"])
print("Minimum Temperature : ",data["main"]["temp_min"])
print("Humidity : ",data["main"]["humidity"])

url="https://wttr.in/{}".format(city)
res = requests.get(url)
print(res.text)
