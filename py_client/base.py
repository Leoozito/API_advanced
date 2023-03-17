import requests

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"

# Aqui é enviado uma response que vai direto para url
get_response = requests.get(endpoint, params={"abc":123}, json={"query":"Hello world"})
print(get_response.headers)
print(get_response.text)

# print(get_response.json())
# print(get_response.status_code)