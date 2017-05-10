#does not work yet(indoor and outdoor)
#contact: jachermocilla@gmail.com


import time
from dronekit import connect, VehicleMode
vehicle = connect('udp:127.0.0.1:14551', wait_ready=True)

# Function to arm and then takeoff to a user specified altitude
def arm_and_takeoff(aTargetAltitude):

  print "Basic pre-arm checks"
  # Don't let the user try to arm until autopilot is ready
  #while not vehicle.is_armable:
  #  print " Waiting for vehicle to initialise..."
  #  time.sleep(1)
        
  print "Arming motors"
  # Copter should arm in GUIDED mode
  #vehicle.mode    = VehicleMode("STABILIZE")
  vehicle.mode    = VehicleMode("GUIDED")

  vehicle.armed   = True

  while not vehicle.armed:
    print " Waiting for arming..."
    time.sleep(1)

  print "Taking off!"
  vehicle.simple_takeoff(aTargetAltitude) # Take off to target altitude
  #vehicle.commands.takeoff(aTargetAltitude) # Take off to target altitude

  # Check that vehicle has reached takeoff altitude
  while True:
    print " Altitude: ", vehicle.location.global_relative_frame.alt 
    #Break and return from function just below target altitude.        
    if vehicle.location.global_relative_frame.alt>=aTargetAltitude*0.95: 
      print "Reached target altitude"
      break
    time.sleep(1)

#for indoor flying
#vehicle.parameters['AHRS_GPS_USE']=0

# Initialize the takeoff sequence to 2.0m
arm_and_takeoff(3.0)

print("Take off complete")

print("Now let's land")
vehicle.mode = VehicleMode("LAND")

# Close vehicle object
vehicle.close()


