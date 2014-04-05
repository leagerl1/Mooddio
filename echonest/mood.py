import pyen
import requests
import json

en = pyen.Pyen("KDS5VIPB1DQPBQKR6")

ec_url = 'http://developer.echonest.com/api/v4/playlist/static'
ec_params = {'api_key': 'KDS5VIPB1DQPBQKR6','mood':'angry','type': 'artist-description','results': '20','bucket': ['id:rdio-US', 'tracks']}
ec_r = requests.get(ec_url, params=ec_params)

'''api_key=KDS5VIPB1DQPBQKR6&mood=angry&type=artist-description&results=20&bucket=id:rdio-US&bucket=tracks')'''

#print r.content
tracks = []
data = json.loads(ec_r.text)

for i in range(len(data['response']['songs'])):
    if len(data['response']['songs'][i]['tracks']) > 0:
        tracks.append(data['response']['songs'][i]['tracks'][0]['foreign_id'][14:])

print tracks
