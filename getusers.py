import base64
import json
import requests


with open('config.json') as config_file:
    data = json.load(config_file)

user = data['username']
apikey = data['apikey']
auth_token = user + ":" + apikey

base64_auth_token_bytes = base64.b64encode(bytes(auth_token, 'utf-8'))
base64_auth_token = str(base64_auth_token_bytes, 'utf-8')

baseUrl = data['url']
endpoint = '/rest/api/3/users/search'
fullUrl = baseUrl + endpoint

headers = {
   "Authorization": "Basic " + base64_auth_token,
   "Accept": "application/json"
}

r = requests.get(fullUrl, headers=headers)

print(json.dumps(json.loads(r.text), sort_keys=True, indent=4, separators=(",", ": ")))

r_json = json.loads(r.text)

for i in r_json:
    if i['accountType'] == "atlassian":
        print(i['accountId'], " => ", i['displayName'])
