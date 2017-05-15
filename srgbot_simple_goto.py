#!/usr/bin/env python
# -*- coding: utf-8 -*-


from dronekit import connect, VehicleMode, LocationGlobalRelative
import time
import math


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
#################################################################################
targetLatitude=14.1601549;
targetLongitude=121.2420353;

#location ics front physci
#targetLatitude=14.1646794;
#targetLongitude=121.2418919;

flightAltitude=5;
target=LocationGlobalRelative(targetLatitude, targetLongitude, flightAltitude);

homeLatitude=0;
homeLongitude=0;
home=LocationGlobalRelative(homeLatitude, homeLongitude, flightAltitude);

airspeed=3
mission_groundspeed=1

distance=0
################################################################################



def get_distance_meters(aLocation1, aLocation2):
    """
    Returns the ground distance in metres between two `LocationGlobal` or `LocationGlobalRelative` objects.

    This method is an approximation, and will not be accurate over large distances and close to the
    earth's poles. It comes from the ArduPilot test code:
    https://github.com/diydrones/ardupilot/blob/master/Tools/autotest/common.py
    """
    dlat = aLocation2.lat - aLocation1.lat
    dlong = aLocation2.lon - aLocation1.lon
    return math.sqrt((dlat*dlat) + (dlong*dlong)) * 1.113195e5


def arm_and_takeoff(aTargetAltitude):
    """
    Arms vehicle and fly to aTargetAltitude.
    """
    global home
    global distance

    print "Basic pre-arm checks"
    # Don't try to arm until autopilot is ready
    while not vehicle.is_armable:
        print " Waiting for vehicle to initialise..."
        time.sleep(1)


    #Get the home location
    print "Home: ", vehicle.location.global_relative_frame
    homeLatitude=vehicle.location.global_relative_frame.lat
    homeLongitude=vehicle.location.global_relative_frame.lon
    home=LocationGlobalRelative(homeLatitude, homeLongitude, flightAltitude);

    distance=get_distance_meters(home,target)

    print "Distance: ", distance
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
vehicle.airspeed = airspeed

# sleep so we can see the change in map
#time.sleep(5)

print "Going to target (groundspeed set to 1 m/s) ..."
vehicle.simple_goto(target, groundspeed=mission_groundspeed)

# sleep so we can see the change in map
print "Sleep: ",int(distance/mission_groundspeed)
time.sleep(int(distance/mission_groundspeed)+5)

print "Going home  (groundspeed set to 1 m/s) ..."
vehicle.simple_goto(home, groundspeed=mission_groundspeed)

# sleep so we can see the change in map
time.sleep(int(distance/mission_groundspeed)+5)

vehicle.mode = VehicleMode("LAND")

while vehicle.armed:      
   print " Waiting to land and disarm..."
   print " Altitude: ", vehicle.location.global_relative_frame.alt
   time.sleep(1)


vehicle.mode = VehicleMode("STABILIZE")
vehicle.armed = False

#Close vehicle object before exiting script
print "Closing vehicle object."
vehicle.close()

# Shut down simulator if it was started.
if sitl is not None:
    sitl.stop()
