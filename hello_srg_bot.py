connection_string = "udp:127.0.0.1:14551"
connection_string = "udp:10.0.0.2:6000"

# Import DroneKit-Python
from dronekit import connect, VehicleMode
import time

# Connect to the Vehicle.
print("Connecting to vehicle on: %s" % (connection_string,))
vehicle = connect(connection_string, wait_ready=True)

# Get some vehicle attributes (state)
print "Get some vehicle attribute values:"
print " GPS: %s" % vehicle.gps_0
print " Battery: %s" % vehicle.battery
print " Last Heartbeat: %s" % vehicle.last_heartbeat
print " Is Armable?: %s" % vehicle.is_armable
print " System status: %s" % vehicle.system_status.state
#print " Mode: %s" % vehicle.mode.name    # settable

vehicle.mode = VehicleMode("GUIDED")
time.sleep(5)
print " Mode: %s" % vehicle.mode.name    # settable


vehicle.mode = VehicleMode("STABILIZE")
time.sleep(5)
print " Mode: %s" % vehicle.mode.name    # settable

# Close vehicle object before exiting script
vehicle.close()

print("Completed")
