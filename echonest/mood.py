import pyen
en = pyen.Pyen("KDS5VIPB1DQPBQKR6")

response = en.get('playlist/static/', artist='weezer',type='artist-radio')
for i, song in enumerate(response['songs']):
    print "%d %-32.32s %s" % (i,song['artist_name'], song['title'])
