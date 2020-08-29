#!/usr/bin/python3
import getpass
import random as rnd
from os import listdir
from os import system


user = getpass.getuser()
wallpapers = [x for x in listdir(f"/home/{user}/Pictures/wallpapers")]
wallpapers = sorted(wallpapers)
wallpaper  = wallpapers[rnd.randint(0, len(wallpapers) - 1)]


if __name__ == '__main__':
	system("nitrogen --set-zoom-fill /home/${USER}/Pictures/wallpapers/" + wallpaper + " &")
