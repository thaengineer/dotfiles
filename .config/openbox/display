#!/bin/bash
intern=LVDS1
extern=HDMI1

if xrandr | grep "$extern disconnected"; then
	xrandr --output "$intern" --mode 1366x768 --rate 60.07 --output "$extern" --off
else
	xrandr --output "$intern" --primary --mode 1366x768 --rate 60.07 --output "$extern" --right-of "$intern" --auto
fi
