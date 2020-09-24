import os
import mutagen

import random
import string
# from mutagen.id3 import ID3, TIT2
from mutagen.id3 import ID3, ID3NoHeaderError
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from googletrans import Translator

translator = Translator()

# directory = '/media/pydev/backup/kiraw/rawwa/'
# directory = '/home/pydev/open-dj/static/music/kimha'
# directory = '/home/pydev/sorting/regga'
directory = '/home/pydev/Downloads/Telegram Desktop'
# directory = '/home/pydev/Downloads/vksaver'
# directory = '/home/pydev/tagged.muson/kimsa'

default_prefix = directory[-5:]
os.chdir(directory)

def file_renamer():
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        print(filename)
        try:
            audio = EasyID3(filename)
        except ID3NoHeaderError:
            tags = ID3()
            tags.save(filename)
            audio = EasyID3(filename)
        # to something with tags


        title : string = (audio.setdefault('composer',[''.join(random.choices(string.ascii_uppercase + string.digits, k=10))])[0]).strip().lower().replace('-',' ')
        # if title is None or title == '':
        #     title = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        # audio['composer'] = title
        #title = translator.translate(title).text + '-' + title
        print(filename)
        rank = (audio.setdefault('artist','salsa-5'))[0][6:7]
        fulltitle = f"{audio['genre'][0]}-{str(rank)}-{title}"
        # print(rank, filename, fulltitle)

        audio['title'] = fulltitle
        audio.save()

        try:
            os.rename(filename, fulltitle + '.mp3')
        except:
            os.rename(filename, fulltitle + ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))+ '.mp3')

def update_tags_filename():
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        print(filename)
        audio = EasyID3(filename)
        title : string = (audio['composer'][0]).strip().lower().replace('-',' ')

        if title is None or title == '':
            title = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        #title = translator.translate(title).text + '-' +
        audio['composer'] = title
        fulltitle = '{}-{}'.format(audio['genre'][0], title)
        print(filename, fulltitle)
        audio['title'] = fulltitle
        audio['composer']=title
        audio.save()
        try:
            os.rename(filename, fulltitle + '.mp3')
        except:
            os.rename(filename, fulltitle + ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))+ '.mp3')

def backup_meta():
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        try:
            audio = EasyID3(filename)
        except ID3NoHeaderError:
            tags = ID3()
            tags.save(filename)
            audio = EasyID3(filename)
        # to something with tags
        all_meta : string = f"{filename}-{audio.setdefault('title',[''])[0]}-{audio.setdefault('artist',[''])[0]}"
        audio['albumartist'] = all_meta
        #audio['composer'] = all_meta
        audio['composer'] = audio.setdefault('title',[all_meta])[0]
        print(audio.setdefault('title',[''])[0])
        audio.save()

if __name__=='__main__':
   file_renamer()