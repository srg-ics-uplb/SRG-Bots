#SRG-Bots

##IP Addresses

Bot : 10.0.0.1
Netbook/Labptop (for DroneKit, OpenCV):  10.0.0.2
Tablet (for Tower): 10.0.0.3

##Run mavproxy on netbook
mavproxy.py --master udp:10.0.0.2:6000 --out 10.0.0.3:14550 --out
127.0.0.1:14551
