BASE_URL = " https://trackapi.nutritionix.com"
exercise_url = "/v2/natural/exercise"

import requests

header= "x-7965d5be-jwt -c5b78ebf2416d9f5e844c6ce2b20a80c"

exer_url = BASE_URL + exercise_url

header = {
    "x-app-id":"7965d5be",
    "x-app-key":"c5b78ebf2416d9f5e844c6ce2b20a80c",
    "x-remote-user-id":"0",
}

data = {
    "query": "I ran for 10 km in 1 hr",
    "gender":"male",
    "weight_kg":83,
    "height_cm":165,
    "age":45,

}


response=requests.post(url=exer_url,headers=header, data=data)
print(response.json())
