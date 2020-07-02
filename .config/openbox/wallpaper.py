#!/usr/bin/python3

import os
import time
import random as rnd

wallpapers = [
	"bg-1.jpg",
	"bg-2.jpg",
	"bg-3.jpg"
]


while(True):
	wallpaper = wallpapers[rnd.randint(0, len(wallpapers) - 1)]
	os.system("nitrogen --set-zoom-fill /home/$USER/Pictures/" + wallpaper + " &")
	time.sleep(600)
