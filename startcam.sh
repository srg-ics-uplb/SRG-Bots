#!/bin/bash
FILENAME=srgbotcam-`date +"%Y%m%d_%H%M%S"`.avi
DURATION=300


#record video
#sudo avconv -f video4linux2 -i /dev/video0 -s vga -vf transpose=1,transpose=1 -t $DURATION $FILENAME

#sudo avconv -f video4linux2 -r 25 -i /dev/video0 -f alsa -i plughw:C525,0 -ar 22050 -ab 64k -strict experimental -async 1 -acodec aac -vcodec mpeg4 -y webcam.mp4

#streaming and recording
#To view: $vlc rtp://0.0.0.0:1234
#sudo avconv -f video4linux2 -s 160x120 -i /dev/video0 -vcodec mpeg2video -r 25 -vf transpose=1,transpose=1 -pix_fmt yuv420p -me_method epzs -b 2600k -bt 256k -f rtp rtp://10.0.0.3:1234
sudo avconv -f video4linux2 -s 160x120 -i /dev/video0 -vcodec mpeg2video -r 25 -pix_fmt yuv420p -me_method epzs -b 2600k -bt 256k -f rtp rtp://10.0.0.3:1234
