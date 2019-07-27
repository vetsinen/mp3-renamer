import eyed3
import os

# a = eyed3.load('/media/pydev/pub/pub/openair/hip/hip-Piggy Bank.mp3')
path = '/home/pydev/Music/chaca/'
os.chdir(path)
filename = 'chaca-v5-fever.mp3'
a = eyed3.load(filename)

print()
a.tag.comment = 'fever'
a.tag.genre ='rock'
a.tag.save()

# os.rename(filename, '{}-{}-{}.mp3'.format('chaca',a.tag.BPM,a.tag.title))
