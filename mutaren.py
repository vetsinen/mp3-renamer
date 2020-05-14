import os
import mutagen

import random
import string
# from mutagen.id3 import ID3, TIT2
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from googletrans import Translator

translator = Translator()

# directory = '/media/pydev/backup/kiraw/rawwa/'
directory = '/home/pydev/open-dj/static/music/kimba'
directory = '/home/pydev/Downloads/Telegram Desktop/bacha'
default_prefix = directory[-5:]
os.chdir(directory)

def file_renamer():
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        audio = EasyID3(filename)
        title : string = (audio['title'][0]).lower().replace('-',' ')
        # if v[0] != 'v' or len(v) != 2:
        #     v = 'v5'
        #     audio['artist'] = v
        #album = audio['album'][0]

        if title is None or title == '':
            title = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        audio['composer'] = title
        #title = translator.translate(title).text + '-' + title
        fulltitle = '{}-{}'.format(default_prefix, title)
        print(filename, fulltitle)
        audio['title'] = fulltitle
        audio.save()
        try:
            os.rename(filename, fulltitle + '.mp3')
        except:
            os.rename(filename, fulltitle + ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))+ '.mp3')


if __name__=='__main__':
    file_renamer()