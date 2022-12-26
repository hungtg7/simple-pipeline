import requests
import json
import sys

tf_url = "http://0.0.0.0:8000/app"
l_url = "http://0.0.0.0:8001/app"

payload = json.dumps({
  "source_name": sys.argv[1],
  "date": sys.argv[2],
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", tf_url, headers=headers, data=payload)

print(response.text)

response = requests.request("POST", l_url, headers=headers, data=payload)

print(response.text)
