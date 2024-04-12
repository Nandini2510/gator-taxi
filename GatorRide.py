class Ride:
    def __init__(self, rideNumber, rideCost, tripDuration):
        self.rideNumber = rideNumber
        self.rideCost = rideCost
        self.tripDuration = tripDuration

#This method is defined to compare two Ride objects and return True if self is less than other_ride according to some criteria.

    def less_than(self, other_ride):
        #If the rideCost of self is less than the rideCost of other_ride, then self is considered less than other_ride. So, the method returns True.
        if self.rideCost < other_ride.rideCost:
            return True
        #If the rideCost of self is greater than the rideCost of other_ride, then self is considered greater than other_ride. So, the method returns False.
        elif self.rideCost > other_ride.rideCost:
            return False
        #If the rideCost of self is equal to the rideCost of other_ride, then we need to compare the tripDuration of the two rides to determine which one is less than the other.
        elif self.rideCost == other_ride.rideCost:
            if self.tripDuration > other_ride.tripDuration:
                return False
            else:
                return True
