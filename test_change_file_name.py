import os
from glob import glob

files = glob("../../imageset/*/*/*.*")
for name in files:
   if not os.path.isdir(name):
       print(name)
       src = os.path.splitext(name) 
       os.rename(name,src[0]+".jpeg")