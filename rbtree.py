class Rbt:
    def __init__(self, ride, min_heap_node):
        self.ride = ride
        self.parent = None  # parent node
        self.left = None  # left node
        self.right = None  # right node
        self.color = 1  # 1=red , 0 = black
        self.min_heap_node = min_heap_node


class RBTree:
    def __init__(self):
        self.null_node = Rbt(None, None)
        self.null_node.left = None
        self.null_node.right = None
        self.null_node.color = 0
        self.root = self.null_node

    # getRide function takes the input as key which is rideNumber and then it searches the rideNumber if it has in the red black tree and returns the value
    def getRide(self, key):
        temp = self.root

       
        while temp != self.null_node:
            if temp.ride.rideNumber == key:
                return temp
            if temp.ride.rideNumber < key:
                temp = temp.right
            else:
                temp = temp.left

        return None

    # balanceAfterDelete function balances the red black tree properties after deleting a specific node
    def balanceAfterDelete(self, node):
        #
        while node != self.root and node.color == 0:
            if node == node.parent.right:
                parent_sibling = node.parent.left
                if parent_sibling.color != 0:
                    node.parent.color = 1
                    parent_sibling.color = 0
                    self.rightRotate(node.parent)
                    parent_sibling = node.parent.left

                if parent_sibling.right.color == 0 and parent_sibling.left.color == 0:
                    parent_sibling.color = 1
                    node = node.parent
                else:
                    if parent_sibling.left.color != 1:
                        parent_sibling.right.color = 0
                        parent_sibling.color = 1
                        self.leftRotate(parent_sibling)
                        parent_sibling = node.parent.left

                    parent_sibling.color = node.parent.color
                    node.parent.color = 0
                    parent_sibling.left.color = 0
                    self.rightRotate(node.parent)
                    node = self.root
            else:
                parent_sibling = node.parent.right
                if parent_sibling.color != 0:
                    node.parent.color = 1
                    parent_sibling.color = 0
                    self.leftRotate(node.parent)
                    parent_sibling = node.parent.right

                if parent_sibling.right.color == 0 and parent_sibling.left.color == 0:
                    parent_sibling.color = 1
                    node = node.parent
                else:
                    if parent_sibling.right.color != 1:
                        parent_sibling.left.color = 0
                        parent_sibling.color = 1
                        self.rightRotate(parent_sibling)
                        parent_sibling = node.parent.right

                    parent_sibling.color = node.parent.color
                    node.parent.color = 0
                    parent_sibling.right.color = 0
                    self.leftRotate(node.parent)
                    node = self.root

        node.color = 0

#rbtreeTransplant performs transplant operation in red black tree,  it replaces the node 'node' with the node 'child_node' in the red-black tree.
    def rbtreeTransplant(self, node, child_node):
        if node.parent is None:
            self.root = child_node
        elif node == node.parent.right:
            node.parent.right = child_node
        else:
            node.parent.left = child_node
        child_node.parent = node.parent


    def deleteHelper(self, node, key):
        deleteNode = self.null_node
        while node != self.null_node:
            if node.ride.rideNumber == key:
                deleteNode = node
            if node.ride.rideNumber >= key:
                node = node.left
            else:
                node = node.right

        if deleteNode == self.null_node:
            return
        heap_node = deleteNode.min_heap_node
        y = deleteNode
        y_original_color = y.color
        if deleteNode.left == self.null_node:
            x = deleteNode.right
            self.rbtreeTransplant(deleteNode, deleteNode.right)
        elif (deleteNode.right == self.null_node):
            x = deleteNode.left
            self.rbtreeTransplant(deleteNode, deleteNode.left)
        else:
            y = self.minimum(deleteNode.right)
            y_original_color = y.color
            x = y.right
            if y.parent == deleteNode:
                x.parent = y
            else:
                self.rbtreeTransplant(y, y.right)
                y.right = deleteNode.right
                y.right.parent = y

            self.rbtreeTransplant(deleteNode, y)
            y.left = deleteNode.left
            y.left.parent = y
            y.color = deleteNode.color
        if y_original_color == 0:
            self.balanceAfterDelete(x)

        return heap_node
 # It balances the red black tree after inserting the new node, it checks if there are any violations in red black tree and fixes it
    def balanceInsert(self, curr_node):
        while curr_node.parent.color == 1:
            if curr_node.parent == curr_node.parent.parent.left:
                parent_sibling = curr_node.parent.parent.right

                if parent_sibling.color == 0:
                    if curr_node == curr_node.parent.right:
                        curr_node = curr_node.parent
                        self.leftRotate(curr_node)
                    curr_node.parent.color = 0
                    curr_node.parent.parent.color = 1
                    self.rightRotate(curr_node.parent.parent)
                else:
                    parent_sibling.color = 0
                    curr_node.parent.color = 0
                    curr_node.parent.parent.color = 1
                    curr_node = curr_node.parent.parent

            else:
                parent_sibling = curr_node.parent.parent.left
                if parent_sibling.color == 0:
                    if curr_node == curr_node.parent.left:
                        curr_node = curr_node.parent
                        self.rightRotate(curr_node)
                    curr_node.parent.color = 0
                    curr_node.parent.parent.color = 1
                    self.leftRotate(curr_node.parent.parent)
                else:
                    parent_sibling.color = 0
                    curr_node.parent.color = 0
                    curr_node.parent.parent.color = 1
                    curr_node = curr_node.parent.parent

            if curr_node == self.root:
                break
        self.root.color = 0

#This function performs an inorder traversal to and adds all the rides with rideNumbers between low and high to the list
    def fromAndToRides(self, node, low, high, res):
        if node == self.null_node:
            return

        if low < node.ride.rideNumber:
            self.fromAndToRides(node.left, low, high, res)
        if low <= node.ride.rideNumber <= high:
            res.append(node.ride)
        self.fromAndToRides(node.right, low, high, res)
# This function searches for ride between this specific range and returns it in the res
    def rideFromandTo(self, low, high):
        res = []
        self.fromAndToRides(self.root, low, high, res)
        return res

    def minimum(self, node):
        while node.left != self.null_node:
            node = node.left
        return node

# The function performs left operation in red black tree to maintain its properties
    def leftRotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.null_node:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

# The function performs right operation in red black tree to maintain its properties
    def rightRotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.null_node:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

# It performs insertion in red black tree
    def insert(self, ride, min_heap):
        node = Rbt(ride, min_heap)
        node.parent = None
        node.left = self.null_node
        node.right = self.null_node
        node.color = 1

        insertion_node = None
        temp_node = self.root

        while temp_node != self.null_node:
            insertion_node = temp_node
            if node.ride.rideNumber < temp_node.ride.rideNumber:
                temp_node = temp_node.left
            else:
                temp_node = temp_node.right

        node.parent = insertion_node
        if insertion_node is None:
            self.root = node
        elif node.ride.rideNumber > insertion_node.ride.rideNumber:
            insertion_node.right = node
        else:
            insertion_node.left = node

        if node.parent is None:
            node.color = 0
            return

        if node.parent.parent is None:
            return

        self.balanceInsert(node)

    def deleteNode(self, rideNumber):
        return self.deleteHelper(self.root, rideNumber)
