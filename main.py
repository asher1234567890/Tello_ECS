from djitellopy import Tello

# init drone
ashers_slave = Tello()
ashers_slave.connect()

# goes uppppp takeofff
ashers_slave.takeoff()

# goes up 90cm
ashers_slave.move_up(90)


ashers_slave.move_forward(500)
ashers_slave.move_forward(100)
#drone moves forward 500cm then 100cm
ashers_slave.move_left(250)
#instead of rotating the drone moves left 200cm
ashers_slave.move_back(500)
ashers_slave.move_back(100)
#drone moves backwards 500cm then  100cm
ashers_slave.move_right(250)
#drone moves right 250cm
ashers_slave.land()
#drone lands
