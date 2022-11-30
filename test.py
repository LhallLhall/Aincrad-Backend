import requests
import json
from pprint import pprint

url = "https://dir84il2yk.execute-api.us-west-2.amazonaws.com/production/v4/games"

payload = "fields rating, release_dates, genres; limit 20; where rating != null; where genres != null; where release_dates != null; where platforms != null; where summary != null;"
headers = {
  'x-api-key': 'HEQsMFqOnt1zD2q1oLwo36jxVFeiavom57v2F0Ud',
  'Client-ID': 'e4e2unaghoyw3t7zz80w1gteqidkaz',
  'Authorization': 'Bearer ea7k5q6odr0g2osf71krx9dxxa1koi',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

pprint(response.json())

   
extra_kwargs = {'password': {'write_only': True}}

def create(self, validated_data):
    password = validated_data.pop('password', None)
    instance = self.Meta.model(**validated_data)  # as long as the fields are the same, we can just use this
    if password is not None:
        instance.set_password(password)
    instance.save()
    return instance