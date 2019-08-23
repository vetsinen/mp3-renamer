import os
import mutagen

import random
import string
from mutagen.id3 import ID3, TIT2

#directory = '/media/pydev/backup/kiraw/rawwa/'
directory = 'd:/kiraw/rawwa/'
default_prefix = directory[-6:-1] + '-v5-'
os.chdir(directory)

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    print(filename)

    audio = ID3(filename)
    audio.add(TIT2(encoding=3, text="An example"))
    audio.save()
    os.rename(filename, "An example" + '.mp3')
    exit()