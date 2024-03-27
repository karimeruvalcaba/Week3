import requests

url = 'http://localhost:5000/postTest'
data = {'nombre': 'Pepe', 'email': 'pepe@example.com'}  # Example data

response = requests.post(url, json=data)

print(response.text)
