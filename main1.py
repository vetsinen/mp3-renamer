import eyed3

a = eyed3.load('/media/pydev/pub/pub/openair/hip/hip-Piggy Bank.mp3')
print (a.tag.artist)
# a.tag.artist ='hip'
# a.tag.save()
