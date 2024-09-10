import requests

# endpoint
ENDPOINT = 'https://reqres.in/api/users?page=2'

# get endpoint
response = requests.get(ENDPOINT)
data = response.json()
#print(data)


# test if that get endpoint correctly

status_code = response.status_code
print(status_code)

def test_get_endpoint():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200