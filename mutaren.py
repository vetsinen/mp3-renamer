import os
import mutagen

import random
import string
#from mutagen.id3 import ID3, TIT2
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3


#directory = '/media/pydev/backup/kiraw/rawwa/'
directory = 'd:/kiraw/rawwa/'
default_prefix = directory[-6:-1] + '-v5-'
os.chdir(directory)

for file in os.listdir(directory):
    filename = os.fsdecode(file)

    title = "sample"
    audio = EasyID3(filename)
    v = audio['artist'][0]
    if v[0]!='v' or len(v)!=2:
        v='v5'
        audio['artist']=v
    title = audio['composer'][0]
    album = audio['album'][0]
    if title is None or title == '':
        title = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    print(filename, album,  v , title )
    fulltitle = '{}-{}-{}'.format(album, v, title).lower()
    audio['title'] =  fulltitle
    audio.save()
    os.rename(filename, fulltitle + '.mp3')