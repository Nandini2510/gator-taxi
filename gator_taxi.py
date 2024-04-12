import sys

from GatorRide import Ride
from minHeap import MinHeap
from minHeap import MinHeapNode
from rbtree import RBTree, Rbt


  # If a ride with the given ride number already exists in the red-black tree,
 #it prints an error message using the addOutput function, exits the program using sys.exit(0), and returns from the function.


def insertRide(ride, heap, rbt):
    if rbt.getRide(ride.rideNumber) is not None:
        addOutput(None, "Duplicate RideNumber", False)
        sys.exit(0)
        return
    rbt_node = Rbt(None, None)

    #Create a new MinHeapNode object to represent the ride in the binary heap and insert it into the heap and the red-black tree
    min_heap_node = MinHeapNode(ride, rbt_node, heap.curr_size + 1)
    heap.insert(min_heap_node)
    rbt.insert(ride, min_heap_node)



def addOutput(ride, message, list):

#Open the file named "output_file.txt" in "append" mode and assign it to the variable file using a with statement to ensure proper file handling
    with open("output_file.txt", "a") as file:

        #If the ride parameter is None, write the message parameter followed by a newline character to the file.
        if ride is None:
            file.write(message + "\n")
        else:
        # Else you perform the following operation depending on the case
            message = ""
            if not list:
                message += ("(" + str(ride.rideNumber) + "," + str(ride.rideCost) + "," + str(ride.tripDuration) + ")\n")
            else:
                if len(ride) == 0:
                    message += "(0,0,0)\n"
                for i in range(len(ride)):
                    if i != len(ride) - 1:
                        message = message + ("(" + str(ride[i].rideNumber) + "," + str(ride[i].rideCost) + "," + str(
                            ride[i].tripDuration) + "),")
                    else:
                        message = message + ("(" + str(ride[i].rideNumber) + "," + str(ride[i].rideCost) + "," + str(
                            ride[i].tripDuration) + ")\n")
# Write the final message string to the file
            file.write(message)

#This method calls the getRide method of the rbt instance, passing in the rideNumber argument. This method searches the red-black tree for a node with a key that matches rideNumber and returns the corresponding MinHeapNode object. The result is assigned to the variable res

def print(rideNumber, rbt):
    res = rbt.getRide(rideNumber)
    if res is None:
        addOutput(Ride(0, 0, 0), "", False)
    else:
        addOutput(res.ride, "", False)

# This method calls the rideFromandTo method of the rbt instance, passing in the l and h arguments. This method searches the red-black tree for nodes whose keys are within the range [l, h] and returns a list of corresponding MinHeapNode objects. The result is assigned to the variable list.
def printRange(l, h, rbt):
    list = rbt.rideFromandTo(l, h)
    addOutput(list, "", True)

# This function gets the lowest ride from the min heap and then pops it out
def getNextRide(heap, rbt):
    if heap.curr_size != 0:
        popped_node = heap.pop()
        rbt.deleteNode(popped_node.ride.rideNumber)
        addOutput(popped_node.ride, "", False)
    else:
        addOutput(None, "No active ride requests", False)


# Deletes the ride from both the data structures, if the ride doesn't exist it ignores it
def cancelRide(ride_number, heap, rbt):
    heap_node = rbt.deleteNode(ride_number)
    if heap_node is not None:
        heap.delete_element(heap_node.min_heap_index)

# Updates the ride by taking rideNumber and new_duration parameters
def updateRide(rideNumber, new_duration, heap, rbt):
    rbt_node = rbt.getRide(rideNumber)
    if rbt_node is None:
        print("")
        # updates the new_tripDuration for the specific rideNumber
    elif new_duration <= rbt_node.ride.tripDuration:
        heap.update_element(rbt_node.min_heap_node.min_heap_index, new_duration)

        #cancel the existing ride and a new ride request would be created with a penalty of 10 on existing rideCost
    elif rbt_node.ride.tripDuration < new_duration <= (2 * rbt_node.ride.tripDuration):
        cancelRide(rbt_node.ride.rideNumber, heap, rbt)
        insertRide(Ride(rbt_node.ride.rideNumber, rbt_node.ride.rideCost + 10, new_duration), heap, rbt)
    else:
        #cancels the Ride
        cancelRide(rbt_node.ride.rideNumber, heap, rbt)


if __name__ == "__main__":
    heap = MinHeap() # Create an instance of the MinHeap class to store ride requests
    rbt = RBTree()  # Create an instance of the RBTree class to store ride requests
    filename = sys.argv[1] # Get the input filename from command line arguments
    file = open(filename)  # Open the input file in read mode
    fout = open("output_file.txt", "w")  # Create the output file in write mode, or truncate it if it exists

    # Loop over each line in the input file
    for s in file.readlines():
        n = []
        # Parse the ride information from the line
        for num in s[s.index("(") + 1:s.index(")")].split(","):
            if num != '':
                n.append(int(num))
                # Check what operation needs to be performed based on the first word in the line
        if "Insert" in s:
            insertRide(Ride(n[0], n[1], n[2]), heap, rbt) # Insert a new ride request
        elif "Print" in s:
            if len(n) == 1:
                print(n[0], rbt) # Print information about a single ride request
            elif len(n) == 2:
                printRange(n[0], n[1], rbt) # Print information about ride requests within a certain range of ride numbers
        elif "UpdateTrip" in s:
            updateRide(n[0], n[1], heap, rbt) # Update the trip duration of a ride request
        elif "GetNextRide" in s:
            getNextRide(heap, rbt)  # Get the next ride request to be serviced
        elif "CancelRide" in s:
            cancelRide(n[0], heap, rbt) # Cancel a ride request and remove it from the heap and tree data structures

