import pyen
import requests
en = pyen.Pyen("KDS5VIPB1DQPBQKR6")

response = en.get('playlist/static/', artist='weezer',type='artist-radio')
for i, song in enumerate(response['songs']):
    print "%d %-32.32s %s" % (i,song['artist_name'], song['title'])

r = requests.get('http://developer.echonest.com/api/v4/song/search?api_key=KDS5VIPB1DQPBQKR6&format=json&results=1&artist=radiohead&title=karma%20police&bucket=id:rdio-US&bucket=tracks')

r.text
print r.text

#http://developer.echonest.com/api/v4/song/search?api_key=YOUR_API_KEY&format=json&results=1&artist=radiohead&title=karma%20police&bucket=id:rdio-US&bucket=tracks

#http://developer.echonest.com/api/v4/song/search?api_key=YOUR_API_KEY&format=json&results=1&artist=radiohead&title=karma%20police&bucket=id:rdio-US&bucket=tracks
