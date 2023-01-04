# username - avishays
# id1      - 208748665
# name1    - Avishay Spitzer
# id2      - 206476079
# name2    - Dory Grossman

import random

"""A class representing a node in an AVL tree"""


class AVLNode(object):
    """Constructor, you are allowed to add more fields.

    @type value: str
    @param value: data of your node
    """

    def __init__(self, value):
        self.value = value
        self.left: AVLNode = None
        self.right: AVLNode = None
        self.parent: AVLNode = None
        self.height: int = -1  # Balance factor
        self.size: int = 0  # size of node

    """returns the left child
    @rtype: AVLNode
    @returns: the left child of self, None if there is no left child
    @complexity: O(1)
    """

    def getLeft(self):
        return self.left

    """returns the right child

    @rtype: AVLNode
    @returns: the right child of self, None if there is no right child
    @complexity: O(1)
    """

    def getRight(self):
        return self.right

    """returns the parent 

    @rtype: AVLNode
    @returns: the parent of self, None if there is no parent
    @complexity: O(1)
    """

    def getParent(self):
        return self.parent

    """return the value

    @rtype: str
    @returns: the value of self, None if the node is virtual
    @complexity: O(1)
    """

    def getValue(self):
        return self.value

    """returns the height

    @rtype: int
    @returns: the height of self, -1 if the node is virtual
    @complexity: O(1)
    """

    def getHeight(self):
        return self.height

    """returns the Balance factor 

    @rtype: int
    @returns: the balance factor of self, 0 if the node is virtual
    @complexity: O(1)
    """
    def getBF(self):
        return self.getLeft().getHeight() - self.getRight().getHeight()

    """returns the size

    @rtype: int
    @returns: the size of the tree rooted by self, 0 if the node is virtual
    @complexity: O(1)
        """
    def getSize(self):
        return self.size

    """sets left child

    @type node: AVLNode
    @param node: a node
    @complexity: O(1)
    """

    def setLeft(self, node):
        self.left = node

    """sets right child

    @type node: AVLNode
    @param node: a node
    @complexity: O(1)   
    """

    def setRight(self, node):
        self.right = node

    """sets parent

    @type node: AVLNode
    @param node: a node
    @complexity: O(1)
    """

    def setParent(self, node):
        self.parent = node

    """sets value

    @type value: str
    @param value: data
    @complexity: O(1)
    """

    def setValue(self, value):
        self.value = value

    """sets height

    @type h: int
    @param h: the height
    @complexity: O(1)   
    """

    def setHeight(self, h):
        self.height = h

    """resets height
    
    update the height of a self
    @complexity: O(1)   
    """

    def resetHeight(self):
        self.height = 1 + max(self.getRight().getHeight(), self.getLeft().getHeight())

    """resets height

    update the size of a self
    @complexity: O(1)   
    """

    def resetSize(self):
        self.size = self.getRight().getSize() + self.getLeft().getSize() + 1

    """returns whether self is not a virtual node 

    @rtype: bool
    @returns: False if self is a virtual node, True otherwise.
    @complexity: O(1)   
    """

    def isRealNode(self):
        return self.height != -1

    """returns whether self leaf 

    @rtype: bool
    @returns: True if self is a leaf, False otherwise.
    @complexity: O(1)   
    """

    def isLeaf(self):
        return self.isRealNode() and (not self.getLeft().isRealNode()) and (not self.getRight().isRealNode())

    """returns relation between self and self.parent

    @rtype: Str
    @returns: left if self is a left child, right if self is a right child, root otherwise
    @complexity: O(1)   
    """

    def relationToParent(self):
        if self.getParent() is None:
            return "root"
        return "left" if self.getParent().getLeft() == self else "right"

    """sets size

    @type size: int
    @param size: the size
    @complexity: O(1)   
    """

    def setSize(self, size):
        self.size = size

    """sets a virtual 

    @type side: Str
    @param side: which side to place the virtual node (could be both left and right)
    the method will set the child of self as a virtual node 
    @complexity: O(1)   
    """

    def place_virtual_nodes_on_leaf(self, side):
        if side == "both":
            virtual_node1 = AVLNode("")
            virtual_node2 = AVLNode("")
            virtual_node1.setParent(self)
            virtual_node2.setParent(self)
            virtual_node1.setHeight(-1)
            virtual_node2.setHeight(-1)
            virtual_node1.setSize(0)
            virtual_node2.setSize(0)
            self.setLeft(virtual_node1)
            self.setRight(virtual_node2)
        else:
            virtual_node = AVLNode("")
            virtual_node.setParent(self)
            virtual_node.setHeight(-1)
            virtual_node.setSize(0)
            if side == "left":
                self.setLeft(virtual_node)
            else:
                self.setRight(virtual_node)


"""
A class implementing the ADT list, using an AVL tree.
"""


class AVLTreeList(object):
    """
    Constructor, you are allowed to add more fields.
    """

    def __init__(self):
        self.size = 0
        self.root: AVLNode = None  # node of the root of the tree
        # add your fields here
        self.firstNode: AVLNode = None  # node of the first value in the list
        self.lastNode: AVLNode = None  # node of the last value in the list

    """returns whether the list is empty
    
    @rtype: bool
    @returns: True if the list is empty, False otherwise
    @complexity: O(1)
    """

    def empty(self):
        return self.size == 0

    """retrieves the value of the i'th item in the list
    
    @type i: int
    @pre: 0 <= i < self.length()
    @param i: index in the list
    @rtype: str
    @returns: the the value of the i'th item in the list
    @complexity: O(log(n))
    """

    def retrieve(self, i):
        return self.retrieveNode(i).getValue()

    """This method rotates the tree around the given node, to the specified side (either "right" or "left").
    
    @type side: str  
    @param side: the side of rotation
    @type node: AVLNode
    @param node: the rotated node
    @complexity: O(1)
    """

    def rotate(self, side, node):
        parent = node.getParent()
        # Determine the relation of the node being rotated to its parent (either "left", "right", or "root").
        relToPar = node.relationToParent()
        # If the rotation is to be performed to the right:
        if side == "right":
            # Re-wire the connections between the nodes.
            y = node.getLeft()
            node.setLeft(y.getRight())
            node.getLeft().setParent(node)
            y.setRight(node)
            node.setParent(y)
            y.setParent(parent)
            if relToPar != "root":
                if relToPar == "right":
                    parent.setRight(y)
                else:
                    parent.setLeft(y)
            # Update the root of the tree if necessary.
            else:
                self.root = y
        # If the rotation is to be performed to the left:
        else:
            # Re-wire the connections between the nodes.
            y = node.getRight()
            node.setRight(y.getLeft())
            node.getRight().setParent(node)
            y.setLeft(node)
            node.setParent(y)
            y.setParent(parent)
            if relToPar != "root":
                if relToPar == "right":
                    parent.setRight(y)
                else:
                    parent.setLeft(y)
            # Update the root of the tree if necessary.
            else:
                self.root = y
        # Update the size and height of the affected nodes.
        node.resetSize()
        node.resetHeight()
        y.resetSize()
        y.resetHeight()
        # Update the size and height of the parent of the node if it is not the root
        if relToPar != "root":
            parent.resetSize()
            parent.resetHeight()

    """inserts val at position i in the list
    
    @type i: int
    @pre: 0 <= i <= self.length()
    @param i: The intended index in the list to which we insert val
    @type val: str
    @param val: the value we inserts
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    @complexity: O(log(n))
    """

    def insert(self, i, val):
        # Initialize counter for number of rebalanced nodes
        cnt_rebalanced = 0
        # Create a new AVLNode with value 'val'
        new_node = AVLNode(val)
        new_node.place_virtual_nodes_on_leaf("both")
        # If the tree is empty, set the new node as the root
        if self.empty():
            self.root = new_node
            self.root.resetSize()
            self.root.resetHeight()
            self.lastNode = new_node
            self.firstNode = new_node
        # If the tree is not empty, insert the new node at the specified index
        else:
            # If inserting at the start of the tree, set the new node as the left child of the current firstNode
            if i == 0:
                self.firstNode.setLeft(new_node)
                new_node.setParent(self.firstNode)
                self.firstNode = new_node
            # If inserting at the end of the tree, set the new node as the right child of the current lastNode
            elif i == self.size:
                self.lastNode.setRight(new_node)
                new_node.setParent(self.lastNode)
                self.lastNode = new_node
            # If inserting at any other index, retrieve the node at that index and find the appropriate leaf node to insert the new node
            else:
                prev_node = self.retrieveNode(i)
                leaf = self.path_to_leaf(prev_node)
                if leaf[1] == 0:
                    leaf[0].setLeft(new_node)
                else:
                    leaf[0].setRight(new_node)
                new_node.setParent(leaf[0])
            # Rebalance the tree on the way up from the new node
            cnt_rebalanced = self.balance_all_the_way_up(new_node)
        # Increment the size of the tree
        self.size += 1
        # Return the number of rebalanced nodes
        return cnt_rebalanced

    """return the closest leaf that smaller than node

    @type node: AVLNode
    @param node: node that the function return the closest leaf that smaller than it
    @rtype: node
    @returns: the closest leaf that smaller than node
    @rtype: int
    @returns: 0 if the node to return is the input node, 1 else
    @complexity: O(log(n))
    """

    def path_to_leaf(self, node: AVLNode):
        # If the left child of the given node is not a real node
        if not node.getLeft().isRealNode():
            return node, 0  # Return the leaf
        # If the given node has a left child, traverse down to the rightmost leaf node in the left subtree
        p = node.getLeft()
        while p.getRight().isRealNode():
            p = p.getRight()
        return p, 1

    """deletes the i'th item in the list
    
    @type i: int
    @pre: 0 <= i < self.length()
    @param i: The intended index in the list to be deleted
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    @complexity: O(log(n))
    """

    def delete(self, i):
        # Get the node to delete and its parent
        node_to_delete = self.retrieveNode(i)
        parent = node_to_delete.getParent()
        # Update the first and last nodes of the list if needed
        if self.firstNode is node_to_delete:
            self.firstNode = self.successor(node_to_delete)
        if self.lastNode is node_to_delete:
            self.lastNode = self.predecessor(node_to_delete)
        # Determine the relationship of the node to delete with its parent
        rel_to_parent = node_to_delete.relationToParent()
        # Initialize the counter for the number of nodes rebalanced
        cnt_rebalanced = 0
        # If the node to delete is a leaf node, remove it from the tree
        if node_to_delete.isLeaf():
            # If the node to delete is the root, set the root to None and update the size
            if rel_to_parent == "root":
                self.root = None
                self.size = 0
                return 0
            # If the node to delete is a left child, place virtual nodes on the left side of the parent
            elif rel_to_parent == "left":
                parent.place_virtual_nodes_on_leaf("left")
            # If the node to delete is a right child, place virtual nodes on the right side of the parent
            else:
                parent.place_virtual_nodes_on_leaf("right")
            # Reset the height and size of the parent
            parent.resetHeight()
            parent.resetSize()
        # If the node to delete has two children, replace it with its successor and delete the successor
        elif node_to_delete.getRight().isRealNode() and node_to_delete.getLeft().isRealNode():
            successor = self.successor(node_to_delete)
            self.replace_nodes(node_to_delete, successor)
            if self.lastNode == successor:
                self.lastNode = self.predecessor(successor)
            parent = successor.getParent()
            rightSon = successor.getRight()
            rel_to_parent_succ = successor.relationToParent()
            parent.setLeft(rightSon) if rel_to_parent_succ == 'left' else parent.setRight(rightSon)
            rightSon.setParent(parent)
            parent.resetHeight()
            parent.resetSize()
        # If the node to delete has one left child
        elif not node_to_delete.getRight().isRealNode():
            if rel_to_parent == "left":
                parent.setLeft(node_to_delete.getLeft())
                parent.getLeft().setParent(parent)
                parent.resetHeight()
                parent.resetSize()
            elif rel_to_parent == "right":
                parent.setRight(node_to_delete.getLeft())
                parent.getRight().setParent(parent)
                parent.resetHeight()
                parent.resetSize()
            else:
                self.root = node_to_delete.getLeft()
                node_to_delete.getLeft().setParent(None)
                node_to_delete.getLeft().resetHeight()
        # If the node to delete has one right child
        else:
            if rel_to_parent == "left":
                parent.setLeft(node_to_delete.getRight())
                parent.getLeft().setParent(parent)
                parent.resetHeight()
                parent.resetSize()
            elif rel_to_parent == "right":
                parent.setRight(node_to_delete.getRight())
                parent.getRight().setParent(parent)
                parent.resetHeight()
                parent.resetSize()
            else:
                self.root = node_to_delete.getRight()
                node_to_delete.getRight().setParent(None)
                node_to_delete.getRight().resetHeight()

        # count  rebalanced on the way up
        cnt_rebalanced += self.balance_all_the_way_up(parent)
        # decrease tree size by one
        self.size -= 1
        return cnt_rebalanced

    """returns the value of the first item in the list
    
    @rtype: str
    @returns: the value of the first item, None if the list is empty
    @complexity: O(1)
    """

    def first(self):
        # if tree is empty
        if self.empty():
            return None
        return self.firstNode.getValue()

    """returns the value of the last item in the list
    
    @rtype: str
    @returns: the value of the last item, None if the list is empty
    @complexity: O(1)
    """

    def last(self):
        # if tree is empty
        if self.empty():
            return None
        return self.lastNode.getValue()

    """returns an array representing list 
    
    @rtype: list
    @returns: a list of strings representing the data structure
    @complexity: O(n)
    """

    def listToArray(self) -> list:
        tree_size = self.getSize()
        if tree_size == 0:
            return []
        arr = [None for i in range(tree_size)]
        self.listToArrayRec(self.root, arr, 0, tree_size - 1)
        return arr

    """recursive implementation of listToArray

    @type: node: AVLNode
    @param: node: node that rooted the tree representation of the list
    @rtype: list
    @returns: a list of strings representing the data structure rooted by node
    @complexity: O(n)
    """
    def listToArrayRec(self, node, arr, i, j) -> list:
        if i == j:
            arr[i] = node.getValue()
        else:
            node_rnk = node.getLeft().getSize()
            tmp = node_rnk + i
            arr[tmp] = node.getValue()
            if node.getLeft().isRealNode():
                self.listToArrayRec(node.getLeft(), arr, i, tmp - 1)
            if node.getRight().isRealNode():
                self.listToArrayRec(node.getRight(), arr, tmp + 1, j)


    """returns the size of the list 

    @rtype: int
    @returns: the size of the list
    @complexity: O(1)
    """

    def getSize(self):
        return self.size

    """returns the height of the list tree representation 

    @rtype: int
    @returns: the height of the tree
    @complexity: O(1)
    """

    def getTreeHeight(self):
        #  return the height of the root (same as height of the tree)
        return self.root.getHeight()

    """returns the length of the list 

   @rtype: int
   @returns: the length of the list
   @complexity: O(1)
   """
    def length(self):
        return self.size

    """sort the info values of the list
    
    @rtype: list
    @returns: an AVLTreeList where the values are sorted by the info of the original list.
    @complexity:O(nlog(n))
    """

    def sort(self):
        arr = self.listToArray()
        arr, cnt_nones = self.relocate_nones_to_the_end(arr)
        arr = self.merge_sorted(arr, 0, len(arr) - cnt_nones - 1)
        arr.extend([None for i in range(cnt_nones)])
        result = self.build_tree_from_array(arr)
        self.balance_if_needed(result.root)
        return result

    """Sort the given array using the merge sort algorithm.

    @complexity:O(nlog(n))
    """

    def merge_sorted(self, arr: list, i: int, j: int) -> list:
        # Base case: if the array is of length 0 or 1, it is already sorted
        if j < i:
            return []
        if j == i:
            return [arr[i]]
        if j - i == 1:
            return [min(arr[i], arr[j]), max(arr[i], arr[j])]
        # Recursively sort the left and right halves of the array
        return self.merge(self.merge_sorted(arr, i, (i + j) // 2), self.merge_sorted(arr, ((i + j) // 2) + 1, j))

    """merge two given arrays.

    @complexity:O(n+m)
    """
    def merge(self, lst1: list, lst2: list) -> list:
        result = []
        p1, p2 = 0, 0
        while p1 < len(lst1) and p2 < len(lst2):
            if lst1[p1] <= lst2[p2]:
                result.append(lst1[p1])
                p1 += 1
            else:
                result.append(lst2[p2])
                p2 += 1
        for i in range(p1, len(lst1)):
            result.append(lst1[i])
        for i in range(p2, len(lst2)):
            result.append(lst2[i])
        return result

    """
    Relocate the None values to the end of the array and return the resulting array and the count of None values.

    @complexity: O(n)
    """

    def relocate_nones_to_the_end(self, arr: list):
        # Count the number of None values in the array
        cnt_nones = 0
        for val in arr:
            if val is None:
                cnt_nones += 1
        # Relocate the None values to the end of the array
        result_array = [val for val in arr if val is not None]
        result_array.extend([None for _ in range(cnt_nones)])
        return result_array, cnt_nones

    """permute the info values of the list 
    
    @rtype: list
    @returns: an AVLTreeList where the values are permuted randomly by the info of the original list. ##Use Randomness
    @complexity: O(n)
    """

    def permutation(self):
        # Convert the tree to an array
        array_tree = self.listToArray()
        array_result = []
        len_result = len(array_tree)
        for _ in range(len_result):
            # Select a random element from the array
            index = random.randrange(0, len(array_tree))
            # Add the selected element to the result array
            array_result.append(array_tree[index])
            # Swap the selected element with the last element in the array
            array_tree[index], array_tree[-1] = array_tree[-1], array_tree[index]
            # Remove the last element (the one that was just selected) from the array
            array_tree.pop()
        # Build a new tree from the permuted array
        result = self.build_tree_from_array(array_result)
        # Balance the tree if needed
        return result

    """build an AVLTree from given array

    @type array: list
    @param array: list to turn into tree
    @rtype: list
    @returns: an AVLTreeList where the values the elements of the list
    @complexity: O(n)
    """
    def build_tree_from_array(self, array: list):
        result = AVLTreeList()
        if len(array) == 0:
            return result
        result.root = AVLNode(array[len(array)//2])
        # build tree and set its fields
        self.build_tree_from_array_rec(result.root, array, 0, len(array) - 1)
        result.size = result.root.size
        result.first = result.retrieveNode(0)
        result.last = result.retrieveNode(result.size - 1)
        return result

    """recursive implementation of build_tree_from_array with indexing 
    
    @type array: list
    @param array: list to turn into tree
    @type node: AVLNode
    @param node: the node that rooted the tree
    @type i: int
    @param i: index of the first element in the list
    @type j: int
    @param j: index of the last element in the list
    @complexity: O(n)
    """

    def build_tree_from_array_rec(self, node: AVLNode, array: list, i, j):
        # Find the middle element of the subarray
        mid = (i + j) // 2
        # Set the value of the current node to the middle element
        node.setValue(array[mid])
        # If the subarray has only one element, set the left child of the current node to be a virtual node
        if mid == i:
            virtual_node = AVLNode("")
            virtual_node.setParent(node)
            virtual_node.setHeight(-1)
            virtual_node.setSize(0)
            node.setLeft(virtual_node)
        # If the subarray has more than one element, build the left subtree of the current node recursively
        else:
            left = AVLNode("place holder")
            node.setLeft(left)
            left.setParent(node)
            self.build_tree_from_array_rec(left, array, i, mid - 1)
            left.resetSize()
            left.resetHeight()
        # If the subarray has only one element, set the right child of the current node to be a virtual node
        if mid == j:
            virtual_node = AVLNode("")
            virtual_node.setParent(node)
            virtual_node.setHeight(-1)
            virtual_node.setSize(0)
            node.setRight(virtual_node)
        # If the subarray has more than one element, build the right subtree of the current node recursively
        else:
            right = AVLNode("place holder")
            node.setRight(right)
            right.setParent(node)
            self.build_tree_from_array_rec(right, array, mid + 1, j)
            right.resetSize()
            right.resetHeight()
        # Reset the size and height of the current node
        node.resetSize()
        node.resetHeight()

    """concatenates lst to self
    
    @type lst: AVLTreeList
    @param lst: a list to be concatenated after self
    @rtype: int
    @returns: the absolute value of the difference between the height of the AVL trees joined
    @complexity: O(log(n))
    """

    def concat(self, lst):
        lst: AVLTreeList
        # Return 0 if both lists are empty.
        if self.empty() and lst.empty():
            return 0
        # If self list is empty, set the properties of the non-empty list to the empty list
        if self.empty():
            self.root = lst.root
            self.firstNode = lst.firstNode
            self.lastNode = lst.lastNode
            self.size = lst.size
            return lst.root.getHeight() + 1
        # If lst is empty, return the difference of heights
        if lst.empty():
            return self.root.getHeight() + 1
        if self.size == 1:
            lst.insert(0, self.root.getValue())
            self.root = lst.root
            self.firstNode = lst.firstNode
            self.lastNode = lst.lastNode
            self.size = lst.size
            return lst.root.getHeight() - 1
        # Calculate the difference in height between the two lists.
        dif = abs(self.root.getHeight() - lst.root.getHeight())
        first = self.firstNode
        last = lst.lastNode
        connecting_node = self.lastNode
        self.delete(self.length() - 1)
        connecting_node.setParent(None)
        p_self = self.root
        p_lst: AVLNode = lst.root
        parent_node_tree = None
        if p_self.getHeight() < p_lst.getHeight():
            parent_node_tree = lst
            while p_self.getHeight() < p_lst.getHeight():
                p_lst = p_lst.getLeft()
        elif p_self.getHeight() > p_lst.getHeight():
            parent_node_tree = self
            while p_self.getHeight() > p_lst.getHeight():
                p_self = p_self.getRight()
        connecting_node.setRight(p_lst)
        connecting_node.setLeft(p_self)
        if parent_node_tree is None:
            connecting_node.setParent(None)
            self.root = connecting_node
        elif parent_node_tree == self:
            connecting_node.setParent(p_self.getParent())
            p_self.getParent().setRight(connecting_node)
        elif parent_node_tree == lst:
            connecting_node.setParent(p_lst.getParent())
            p_lst.getParent().setLeft(connecting_node)
            self.root = lst.root
        connecting_node.resetSize()
        connecting_node.resetHeight()
        self.firstNode = first
        self.lastNode = last
        self.size += lst.getSize() + 1
        self.balance_all_the_way_up(connecting_node)
        return dif

    """searches for a *value* in the list

    @type val: str
    @param val: a value to be searched
    @rtype: int
    @returns: the first index that contains val, -1 if not found.
    @complexity: O(n)
    """

    def search(self, val):
        if self.root == None:
            return -1
        node = self.search_node_rec(self.root, val)
        if node is None:
            return -1
        else:
            return self.get_node_index(node)


    """recursive implementation of search

    @type val: str
    @param val: a value to be searched
    @type Node: AVLNode
    @param Node: the node that rooted the tree val is search in
    @rtype: int
    @returns: the first index that contains val, -1 if not found.
    @complexity: O(n)
    """
    def search_node_rec(self, node: AVLNode, val):
        if not node.isRealNode():
            return None
        if node.getValue() == val:
            return node
        left = self.search_node_rec(node.getLeft(), val)
        if left is not None:
            return left
        right = self.search_node_rec(node.getRight(), val)
        if right is not None:
            return right
        return

    """
    Returns the index of the given node in the sorted list of nodes in the AVL tree.
    @complexity: O(log(n))
    """

    def get_node_index(self, node: AVLNode):
        # Initialize the sum of sizes to the size of the left subtree of the given node
        sum_size = node.getLeft().getSize()

        # Traverse the tree starting from the given node and adding the size of the left
        # subtree of each parent node to the sum if the current node is a right child
        p = node
        while p.getParent() is not None:
            if p.relationToParent() == "right":
                sum_size += p.getParent().getLeft().getSize() + 1
            p = p.getParent()

        return sum_size


    """returns the successor of given node

    @rtype: AVLNode
    @returns: the successor of given Node, None if node is self.lastNode
    @complexity: O(log(n))
    """
    def successor(self, node):
        if node is self.lastNode:
            return None
        p = node
        if node.getRight().isRealNode():
            p = p.getRight()
            while p.getLeft().isRealNode():
                p = p.getLeft()
            return p
        else:
            while p.relationToParent() == 'right':
                p = p.getParent()
            return p.getParent()


    """returns the predecessor of given node

    @rtype: AVLNode
    @returns: the predecessor of given Node, None if node is self.firstNode
    @complexity: O(log(n))
    """
    def predecessor(self, node):
        if node is self.firstNode:
            return None
        p = node
        if node.getLeft().isRealNode():
            p = p.getLeft()
            while p.getRight().isRealNode():
                p = p.getRight()
            return p
        else:
            while p.relationToParent() == 'left':
                p = p.getParent()
            return p.getParent()

    """returns the root of the tree representing the list

    @rtype: AVLNode
    @returns: the root, None if the list is empty
    @complexity: O(1)
    """

    def getRoot(self):
        return self.root

    """retrieves the value of the i'th item in the list

    @type i: int
    @param i: index in the list
    @rtype: AVLNode
    @returns: the node that its value is i'th item in the list
    @complexity: O(log(n))
    """

    def retrieveNode(self, i) -> AVLNode:
        return self.retrieveNodeRec(self.root, i)

    """recursive implementation of retrieveNode

    @type i: int
    @param i: index in the list
    @type currentNode: AVLNode
    @param currentNode: the node that is searched in
    @rtype: AVLNode
    @returns: the node that its value is i'th item in the list
    @complexity: O(log(n))
    """

    def retrieveNodeRec(self, currentNode, i):
        if currentNode.getLeft().getSize() == i:
            return currentNode
        elif currentNode.getLeft().getSize() > i:
            return self.retrieveNodeRec(currentNode.getLeft(), i)
        return self.retrieveNodeRec(currentNode.getRight(), i - (currentNode.getLeft().getSize() + 1))

    """rebalance the tree upward from a certain node
    
    @type node: AVLNode
    @param node: the node that start the rebalancing
    @complexity: O(log(n))
    """

    def balance_all_the_way_up(self, node: AVLNode) -> int:
        # Initialize a counter for the number of nodes rebalanced to 0.
        cnt_rebalanced = 0
        while node is not None:
            node.resetSize()
            node.resetHeight()
            # Calculate the balance factor (BF) of the current node.
            node_BF = node.getBF()
            if node_BF == 2:
                left_node = node.getLeft()
                left_node_BF = left_node.getBF()
                if left_node_BF >= 0:
                    self.rotate("right", node)
                    cnt_rebalanced += 1
                elif left_node_BF < 0:
                    self.rotate("left", left_node)
                    self.rotate("right", node)
                    cnt_rebalanced += 2
            elif node_BF == -2:
                right_node = node.getRight()
                right_node_BF = right_node.getBF()
                if right_node_BF <= 0:
                    self.rotate("left", node)
                    cnt_rebalanced += 1
                elif right_node_BF > 0:
                    self.rotate("right", right_node)
                    self.rotate("lef", node)
                    cnt_rebalanced += 2
            # Set the current node to its parent.
            node = node.getParent()
        return cnt_rebalanced

    """switch the values of two nodes in the tree

    @type node1, node2: AVLNode
    @param node1, node2: the nodes whose values are switched
    @complexity: O(1)
    """
    def replace_nodes(self, node1: AVLNode, node2: AVLNode):
        tmp_value = node1.getValue()
        node1.setValue(node2.getValue())
        node2.setValue(tmp_value)

    def append(self, val):
        self.insert(self.length(), val)

