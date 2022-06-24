#Api is a tool that allows us to get data from a database and then use it

import requests

response = requests.get("http://randomfox.ca/floof")
print(response.status_code)
print(response.text)
fox = response.json()
print(fox['image'])
