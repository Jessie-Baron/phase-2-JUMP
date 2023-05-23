import requests

data = requests.post("http://localhost:5000/hello/requests", json={})
print(data, data.text)

login = {
    "username": "Hello",
    "password": "Flask"
}

data = requests.post("http://localhost:5000/login", json=login)
print(data, data.text)