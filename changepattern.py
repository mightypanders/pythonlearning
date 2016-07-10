import os
import random

mypath = "/home/markus/walls/patterns/"
files = os.listdir(os.path.dirname(mypath))
newimg = files[random.randrange(0, len(files))]
fctcall = "feh --bg-tile " + mypath + newimg
os.system(fctcall)
