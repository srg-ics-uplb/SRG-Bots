connection_string = "udp:127.0.0.1:14551"

# Import DroneKit-Python
from dronekit import connect, VehicleMode
import time

def meters_to_feet(meters):
    return meters * 3.2808399


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
print " Mode: %s" % vehicle.mode.name    # settable

while True:
    print " Altitude: ", vehicle.location.global_relative_frame.alt 
    feet=meters_to_feet(vehicle.location.global_relative_frame.alt)
    inches = (feet * 12) % 12
    feet = int(feet)

    print "meters is", feet, "feet", inches, "inches"

    time.sleep(1)

# Close vehicle object before exiting script
vehicle.close()

print("Completed")
