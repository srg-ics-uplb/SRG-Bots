#!/bin/env python

#
# Displays the altitude of the bot
# contact: jachermocilla@gmail.com
#

from dronekit import connect, VehicleMode
import time

connection_string = "udp:127.0.0.1:14551"

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


vehicle.mode = VehicleMode("ALT_HOLD")
vehicle.armed = True

while not vehicle.is_armable:
   print " Waiting for vehicle to initialise..."
   time.sleep(1)

print "Home: ", vehicle.location.global_relative_frame

vehicle.armed = False

# Close vehicle object before exiting script
vehicle.close()


print("Completed")
