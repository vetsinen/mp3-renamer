import os

directory_in_str = '/media/pydev/pub/pub/audiobooks/general/'
directory = os.fsencode(directory_in_str)

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    parts = filename[:-4].lower().split("-")
    print(len(parts), filename, parts)
    if len(parts) == 2:
        dst = parts[1].strip() + '-' + parts[0].strip() + '.mp3'
        print(dst)
        os.rename(directory_in_str+filename,directory_in_str+dst)