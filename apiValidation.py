import json
import requests

endpoint: str = 'https://jsonplaceholder.typicode.com/posts'
response = requests.get(endpoint)

response_body = response.json()
print(response_body)




