#!/bin/bash

# by jachermocilla@gmail.com
#
# Start recording videos using the 
# USB Webcam payload using avconv.
#
# Uncomment the option to use
#


FILENAME=srgbotcam-`date +"%Y%m%d_%H%M%S"`.avi
DURATION=300
VIEWER_IP=10.0.0.2
VIEWER_PORT=1234

#Option 1) record and save video
#sudo avconv -f video4linux2 -i /dev/video0 -s vga -vf transpose=1,transpose=1 -t $DURATION $FILENAME

#Option 2) record and save audio and video
#sudo avconv -f video4linux2 -r 25 -i /dev/video0 -f alsa -i plughw:C525,0 -ar 22050 -ab 64k -strict experimental -async 1 -acodec aac -vcodec mpeg4 -y webcam.mp4

#Option 3) UDP streaming 
#To view: $vlc udp://@0.0.0.0:1234
sudo avconv -f video4linux2 -i /dev/video0 -s qqvga -vf transpose=1,transpose=1 -c:v mpeg4 -f mpegts udp://$VIEWER_IP:$VIEWER_PORT
