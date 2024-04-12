
## Gator Taxi System

This repository contains an implementation of a Gator Taxi System utilizing advanced data structures like Min Heap and Red-Black Tree. The system efficiently manages ride requests, enabling operations such as ride insertion, retrieval, cancellation, and updates.

### Files

- **gatotTaxi.py**
  - Contains the main function to read input and execute corresponding operations.
  
- **minHeap.py**
  - Implements the Min Heap data structure and associated operations.
  
- **redBlackTree.py**
  - Implements the Red-Black Tree data structure and associated operations.
  
- **rideMode.py**
  - Initializes Gator Taxi parameters and handles ride cost comparisons.

### Operations

- **Print(rideNumber)**
  - Retrieves ride details based on the specified ride number.
  
- **Print(rideNumber1, rideNumber2)**
  - Retrieves ride details for a range of ride numbers.
  
- **Insert(rideNumber, rideCost, tripDuration)**
  - Inserts a new ride request into both the Min Heap and Red-Black Tree.

- **GetNextRide()**
  - Retrieves and removes the ride request with the minimum cost (top of the Min Heap).

- **CancelRide(rideNumber)**
  - Cancels a specific ride request by removing it from both data structures.

- **UpdateTrip(rideNumber, new_tripDuration)**
  - Updates the trip duration for a specific ride request and maintains data structure integrity.

### Time and Space Complexity

- **Time Complexity**
  - Operations involving the Red-Black Tree or Min Heap are generally performed in \(O(\log n)\) time, where \(n\) is the number of nodes.

- **Space Complexity**
  - The system has an overall space complexity of \(O(n)\), storing \(n\) nodes across the Min Heap and Red-Black Tree.

### Usage

To use the Gator Taxi System, execute `gatotTaxi.py` and provide input commands as specified in the operations section.

### Note

This system is designed to efficiently manage ride requests using optimal data structures for insertion, retrieval, cancellation, and update operations. The implemented data structures ensure that operations are performed within logarithmic time complexity, making it suitable for real-time applications.

For more details on specific functions and their implementations, refer to individual files (`gatotTaxi.py`, `minHeap.py`, `redBlackTree.py`, `rideMode.py`) within this repository.
