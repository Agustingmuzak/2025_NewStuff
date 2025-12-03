import requests

BASE= "http://127.0.0.1:5000/"

""" response = requests.get(BASE + "helloworld/micalela")
print(response.json()) """

""" response2 = requests.post(BASE + "helloworld")
print(response2.json()) """

response3 = requests.put(BASE + "video/1", {"likes": 10, "name": "me at the zoo", "views": 30})
print(response3.json())

input()

response = requests.get(BASE + "video/1")
print(response.json())