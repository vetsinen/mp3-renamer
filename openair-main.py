import os
import eyed3

import random
import string

# directory = '/home/pydev/Music/regga/'
directory = 'd:/dance/bacya/'
default_prefix = directory[-6:-1]+'-v5-'
print(default_prefix)
os.chdir(directory)

# directory = os.fsencode(directory)
def extract_title():
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        try:
            track = eyed3.load(filename)
            print(filename)

            parts = filename.split('-')
            realtitle = parts[-1].lower().replace('-', '')
            if realtitle.endswith('.mp3'):
                realtitle = realtitle[:-4]
            if realtitle is None:
                realtitle = filename
            print(realtitle)
            track.tag.composer = realtitle
            track.tag.save()
        except Exception:
            print('cant be processed')

def retitle_and_rename():
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        try:
            track = eyed3.load(filename)
            print(filename)
            if not track:
                continue

            if track.tag.artist[0] != 'v':
                track.tag.artist = 'v5'
            realtitle = track.tag.composer

            if realtitle is None:
                realtitle = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
                track.tag.composer = realtitle
            realtitle = realtitle.lower().replace('-', '')
            print(realtitle)
            track.tag.title = '{}-{}-{}'.format(track.tag.album, track.tag.artist,realtitle)
            track.tag.save()
            os.rename(file,track.tag.title+'.mp3')
        except Exception:
            os.rename(file, default_prefix + ''.join(random.choices(string.ascii_uppercase + string.digits, k=10)) +'.mp3')
        finally:
            pass

# extract_title()
retitle_and_rename()