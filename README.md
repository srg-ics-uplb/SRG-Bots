# SRG-Bots

## IP Addresses

Bot: 10.0.0.1

Netbook:  10.0.0.2

Tablet: 10.0.0.3

Make sure that the above IP Address assignments are 
strictly followed. Otherwise, the setup will not work.


## Enable Tower/APM Planner and DroneKit to connect

Activate the dronekit virtual environment on the Netbook
 then run the command below.

This will allow the Tablet to connect to port 14550 and DroneKit to port 14551.

`mavproxy.py --master udp:10.0.0.2:6000 --out 10.0.0.3:14550 --out 127.0.0.1:14551`


