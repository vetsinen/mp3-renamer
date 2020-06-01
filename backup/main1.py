# first, we need to import our essentia module. It is aptly named 'essentia'!
import essentia

# as there are 2 operating modes in essentia which have the same algorithms,
# these latter are dispatched into 2 submodules:
import essentia.standard
import essentia.streaming

# let's have a look at what is in there
# print(dir(essentia.standard))

# we start by instantiating the audio loader:
loader = essentia.standard.MonoLoader(filename='/home/pydev/Music/regga/regga-v5-suelta.mp3')
# and then we actually perform the loading:
audio = loader()