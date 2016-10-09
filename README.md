#SRG-Bots

##IP Addresses

Bot: 10.0.0.1

Netbook/Laptop:  10.0.0.2

Tablet: 10.0.0.3

##Enable Tower/APM Planner and DroneKit to connect
`mavproxy.py --master udp:10.0.0.2:6000 --out 10.0.0.3:14550 --out
127.0.0.1:14551`

The command above should be executed on the Netbook. This will allow the Tablet to connect to port 14550 and DroneKit to port 14551.

