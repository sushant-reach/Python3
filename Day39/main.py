import requests


def test():
    responce = requests.get(url="http://api.open-notify.org/iss-now.json")
    data = responce.json()
    print(data)

para = {
    "lat":18.5204,
    "lon":73.8567,
    "api_key":"e54ec30cad0fd03e30f97f0f15aeeef0",
}

# working
# "https://api.openweathermap.org/data/2.5/weather?q=london,uk&appid=e54ec30cad0fd03e30f97f0f15aeeef0

api_key="e54ec30cad0fd03e30f97f0f15aeeef0"
end_point="https://api.openweathermap.org/data/3.0/onecall"


responce= requests.get(url=end_point,params=para)
data = responce.json()
print(data)
