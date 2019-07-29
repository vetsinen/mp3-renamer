import os
import eyed3

import random
import string

directory = '/home/pydev/Music/regga/'
os.chdir(directory)

# directory = os.fsencode(directory)
def extract_title():
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
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

def retitle_and_rename():
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        track = eyed3.load(filename)
        print(filename)

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

retitle_and_rename()