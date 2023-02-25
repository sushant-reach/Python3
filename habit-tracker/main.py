
import requests

pixela_endpoint = "https://pixe.la/v1/users"
USER_NAME="whatthehell"
TOKEN="dhjhkjiudduuuyieyeu66868765657"

user_param = {
    "token":TOKEN,
    "username":USER_NAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
    }

#response=requests.post(url=pixela_endpoint, json=user_param)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph = {
    "id":"test-graph1",
    "name":"Cycling",
    "unit":"KM",
    "type":"float",
    "color":"shibafu",
}

headers = {
    "X-USER-TOKEN":TOKEN,
}

response=requests.post(graph_endpoint,json=graph,headers=headers)
print(response.text)










