import os
import eyed3

import random
import string

#directory = '/media/pydev/backup/kiraw/rawwa/'
directory = 'd:/kiraw/kim3a/'
default_prefix = directory[-6:-1] + '-v5-'
print(default_prefix)
os.chdir(directory)


# directory = os.fsencode(directory)
def extract_title():
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        print(filename)
        try:
            track = eyed3.load(filename)

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
        print(filename)

        track = eyed3.load(filename)

        if not track:
            print(filename + ' track not processed')
            os.rename(filename, default_prefix + ''.join(
                random.choices(string.ascii_uppercase + string.digits, k=10)) + '.mp3')
            continue

        if track.tag.artist[0] != 'v':
            track.tag.artist = 'v5'

        realtitle = track.tag.composer

        if realtitle is None:
            realtitle = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
            track.tag.composer = realtitle
        realtitle = realtitle.lower().replace('-', '')
        print('real title: ' + realtitle)
        track.tag.title = '{}-{}-{}'.format(track.tag.album, track.tag.artist, realtitle)

        try:
            track.tag.save()
            os.rename(filename, track.tag.title + '.mp3')
        except Exception as e:
            print('TagException happens')
            print('Error! Code: {c}, Message, {m}'.format(c=type(e).__name__, m=str(e)))
            os.rename(filename, 'zzz' + track.tag.title + '.mp3')
        finally:
            pass


# extract_title()
retitle_and_rename()
