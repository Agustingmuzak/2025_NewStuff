import requests

BASE= "http://127.0.0.1:5000/"

""" response = requests.get(BASE + "helloworld/micalela")
print(response.json()) """

""" response2 = requests.post(BASE + "helloworld")
print(response2.json()) """

response3 = requests.put(BASE + "video/1", {"likes": 10})
print(response3.json())