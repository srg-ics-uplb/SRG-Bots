#!/usr/bin/env python
# -*- coding: utf-8 -*-


from dronekit import connect, VehicleMode, LocationGlobalRelative
import time


#Set up option parsing to get connection string
import argparse  
parser = argparse.ArgumentParser(description='Commands vehicle using vehicle.simple_goto.')
parser.add_argument('--connect', 
                   help="Vehicle connection target string. If not specified, SITL automatically started and used.")
args = parser.parse_args()

connection_string = args.connect
sitl = None


#Start SITL if no connection string specified
#if not connection_string:
#    import dronekit_sitl
#    sitl = dronekit_sitl.start_default()
#    connection_string = sitl.connection_string()
connection_string="udp:127.0.0.1:14551";


# Connect to the Vehicle
print 'Connecting to vehicle on: %s' % connection_string
vehicle = connect(connection_string, wait_ready=True)

#Mission parameters
targetLatitude=14.1601549;
targetLongitude=121.2420353;
flightAltitude=5;
target=LocationGlobalRelative(targetLatitude, targetLongitude, flightAltitude);

homeLatitude=0;
homeLongitude=0;
home=LocationGlobalRelative(homeLatitude, homeLongitude, flightAltitude);


def arm_and_takeoff(aTargetAltitude):
    """
    Arms vehicle and fly to aTargetAltitude.
    """
    global home

    print "Basic pre-arm checks"
    # Don't try to arm until autopilot is ready
    while not vehicle.is_armable:
        print " Waiting for vehicle to initialise..."
        time.sleep(1)

    print "Home: ", vehicle.location.global_relative_frame
    homeLatitude=vehicle.location.global_relative_frame.lat
    homeLongitude=vehicle.location.global_relative_frame.lon
    home=LocationGlobalRelative(homeLatitude, homeLongitude, flightAltitude);

        
    print "Arming motors"
    # Copter should arm in GUIDED mode
    
    vehicle.mode = VehicleMode("STABILIZE")
    time.sleep(5)

    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True    

    # Confirm vehicle armed before attempting to take off
    while not vehicle.armed:      
        print " Waiting for arming..."
        time.sleep(1)

    print "Taking off!"
    vehicle.simple_takeoff(aTargetAltitude) # Take off to target altitude

    # Wait until the vehicle reaches a safe height before processing the goto (otherwise the command 
    #  after Vehicle.simple_takeoff will execute immediately).
    while True:
        print " Altitude: ", vehicle.location.global_relative_frame.alt 
        #Break and return from function just below target altitude.        
        if vehicle.location.global_relative_frame.alt>=aTargetAltitude*0.95: 
            print "Reached target altitude!"
            break
        time.sleep(1)

#delay a little
#time.sleep(5)

arm_and_takeoff(flightAltitude)

print "Set default/target airspeed to 3"
vehicle.airspeed = 3

# sleep so we can see the change in map
time.sleep(30)

print "Going to target (groundspeed set to 5 m/s) ..."
vehicle.simple_goto(target, groundspeed=5)

# sleep so we can see the change in map
time.sleep(45)

print "Going home  (groundspeed set to 10 m/s) ..."
vehicle.simple_goto(home, groundspeed=10)

# sleep so we can see the change in map
time.sleep(45)

vehicle.mode = VehicleMode("LAND")

while vehicle.armed:      
   print " Waiting to land and disarm..."
   print " Altitude: ", vehicle.location.global_relative_frame.alt
   time.sleep(1)


#Close vehicle object before exiting script
print "Closing vehicle object."
vehicle.close()

# Shut down simulator if it was started.
if sitl is not None:
    sitl.stop()
