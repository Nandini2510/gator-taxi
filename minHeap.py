class MinHeap:
    def __init__(self):
        self.heap_list = [0]
        self.curr_size = 0
# Insert new elements in min heap and maintains its properties
    def insert(self, ele):
        self.heap_list.append(ele)
        self.curr_size += 1
        self.heapify_up(self.curr_size)

# This operation is used to maintain the heap property after inserting a new element into the heap. 
    def heapify_up(self, p):
        while (p // 2) > 0:
            if self.heap_list[p].ride.less_than(self.heap_list[p // 2].ride):
                self.swap(p, (p // 2))
            else:
                break
            p = p // 2

# It is swapping two elements for maintaining heap properties
    def swap(self, ind1, ind2):
        temp = self.heap_list[ind1]
        self.heap_list[ind1] = self.heap_list[ind2]
        self.heap_list[ind2] = temp
        self.heap_list[ind1].min_heap_index = ind1
        self.heap_list[ind2].min_heap_index = ind2

#Starting from a given node index 'p', the function finds the minimum child node index among the left and right children of the node 'p'. If the value of the minimum child node is less than the value of the node 'p', the function swaps the values of these nodes.
    def heapify_down(self, p):
        while (p * 2) <= self.curr_size:
            ind = self.get_min_child_index(p)
            if not self.heap_list[p].ride.less_than(self.heap_list[ind].ride):
                self.swap(p, ind)
            p = ind
# This method is used to find the index of the child node with the minimum value in a given node's subtree.
    def get_min_child_index(self, p):
        if (p * 2) + 1 > self.curr_size:
            return p * 2
        else:
            if self.heap_list[p * 2].ride.less_than(self.heap_list[(p * 2) + 1].ride):
                return p * 2
            else:
                return (p * 2) + 1

# This method takes in an index p and a new key, and updates the tripDuration of the corresponding ride object in the heap with the new key
    def update_element(self, p, new_key):
        node = self.heap_list[p]
        node.ride.tripDuration = new_key
        if p == 1:
            self.heapify_down(p)
        elif self.heap_list[p // 2].ride.less_than(self.heap_list[p].ride):
            self.heapify_down(p)
        else:
            self.heapify_up(p)

# implementing the delete operation for an element in a min heap data structure


    def delete_element(self, p):

        self.swap(p, self.curr_size)
        
        self.curr_size -= 1
        *self.heap_list, _ = self.heap_list

        self.heapify_down(p)
        
#The heap represents a set of rides that can be taken, and pop returns the shortest ride available.
    def pop(self):

        if len(self.heap_list) == 1:
            return 'No Rides Available'

        root = self.heap_list[1]

        self.swap(1, self.curr_size)
       
        self.curr_size -= 1
        *self.heap_list, _ = self.heap_list

        self.heapify_down(1)

        return root


class MinHeapNode:
    def __init__(self, ride, rbt, min_heap_index):
        self.ride = ride
        self.rbTree = rbt
        self.min_heap_index = min_heap_index
