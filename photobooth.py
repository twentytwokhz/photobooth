#!/usr/bin/python

import time, os, datetime, sys

t = int(str(sys.argv[1]))
seconds = int(str(sys.argv[2]))
print "Photo shooting time is " + sys.argv[2] + " seconds"
t_end = time.time() + seconds
print "Each " + sys.argv[1] + " seconds a photo is taken"
os.system("gphoto2 --set-config imagesize=2")

while time.time() < t_end:
  img = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + '.jpg';
  print "Photo taken: " + img
  os.system("gphoto2 --capture-image-and-download --filename photobooth/" + img);
  time.sleep(t)

os.system("convert -resize 800x600 photobooth/*.jpg photobooth/result.gif")
os.system("python fb.py photobooth/result.gif")
