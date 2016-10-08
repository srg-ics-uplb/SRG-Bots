from dronekit import connect

#This setup assumes that mavproxy is running
#example:
# mavproxy.py --master udp:10.0.0.2:6000 --out 127.0.0.1:14550 --out 127.0.0.1:14551


# Connect to the Vehicle (in this case a UDP endpoint)
# connect string must be IP of GCS
vehicle = connect('udp:127.0.0.1:14551', wait_ready=True)
