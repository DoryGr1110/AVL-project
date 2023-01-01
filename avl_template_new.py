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
        self.size: int = 0

    """returns the left child
    @rtype: AVLNode
    @returns: the left child of self, None if there is no left child
    """

    def getLeft(self):
        return self.left

    """returns the right child

    @rtype: AVLNode
    @returns: the right child of self, None if there is no right child
    """

    def getRight(self):
        return self.right

    """returns the parent 

    @rtype: AVLNode
    @returns: the parent of self, None if there is no parent
    """

    def getParent(self):
        return self.parent

    """return the value

    @rtype: str
    @returns: the value of self, None if the node is virtual
    """

    def getValue(self):
        return self.value

    """returns the height

    @rtype: int
    @returns: the height of self, -1 if the node is virtual
    """

    def getHeight(self):
        return self.height

    def getBF(self):
        return self.getLeft().getHeight() - self.getRight().getHeight()

    def getSize(self):
        return self.size

    """sets left child

    @type node: AVLNode
    @param node: a node
    """

    def setLeft(self, node):
        self.left = node

    """sets right child

    @type node: AVLNode
    @param node: a node
    """

    def setRight(self, node):
        self.right = node

    """sets parent

    @type node: AVLNode
    @param node: a node
    """

    def setParent(self, node):
        self.parent = node

    """sets value

    @type value: str
    @param value: data
    """

    def setValue(self, value):
        self.value = value

    """sets the balance factor of the node

    @type h: int
    @param h: the height
    """

    def setHeight(self, h):
        self.height = h

    def resetHeight(self):
        self.height = 1 + max(self.getRight().getHeight(), self.getLeft().getHeight())

    def resetSize(self):
        self.size = self.getRight().getSize() + self.getLeft().getSize() + 1

    """returns whether self is not a virtual node 

    @rtype: bool
    @returns: False if self is a virtual node, True otherwise.
    """

    def isRealNode(self):
        return self.height != -1

    def isLeaf(self):
        return self.isRealNode() and (not self.getLeft().isRealNode()) and (not self.getRight().isRealNode())

    def relationToParent(self):
        if self.getParent() is None:
            return "root"
        return "left" if self.getParent().getLeft() == self else "right"

    def setSize(self, size):
        self.size = size

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
        self.root: AVLNode = None
        # add your fields here
        self.firstNode: AVLNode = None
        self.lastNode: AVLNode = None

    """returns whether the list is empty
    
    @rtype: bool
    @returns: True if the list is empty, False otherwise
    """

    def empty(self):
        return self.size == 0

    """retrieves the value of the i'th item in the list
    
    @type i: int
    @pre: 0 <= i < self.length()
    @param i: index in the list
    @rtype: str
    @returns: the the value of the i'th item in the list
    """

    def retrieve(self, i):
        if 0 > i or i >= self.length():
            return None
        return self.retrieveNode(i).getValue()

    def rotate(self, side, node):
        if side == "right":
            parent = node.getParent()
            relToPar = node.relationToParent()
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
            else:
                self.root = y
        else:
            parent = node.getParent()
            relToPar = node.relationToParent()
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
            else:
                self.root = y
        node.resetSize()
        node.resetHeight()
        y.resetSize()
        y.resetHeight()
        if relToPar != "root":
            parent.resetSize()
            parent.resetHeight()

    """inserts val at position i in the list
    
    @type i: int
    @pre: 0 <= i <= self.length()
    @param i: The intended index in the list to which we insert val
    @type val: str
    @param val: the value we inserts
    @rtype: list
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    def insert(self, i, val):
        cnt_rebalanced = 0
        new_node = AVLNode(val)
        new_node.place_virtual_nodes_on_leaf("both")
        if self.empty():
            self.root = new_node
            self.root.resetSize()
            self.root.resetHeight()
            self.lastNode = new_node
            self.firstNode = new_node
        else:
            if i == 0:
                self.firstNode.setLeft(new_node)
                new_node.setParent(self.firstNode)
                self.firstNode = new_node
            elif i == self.size:
                self.lastNode.setRight(new_node)
                new_node.setParent(self.lastNode)
                self.lastNode = new_node
            else:
                prev_node = self.retrieveNode(i)
                leaf = self.path_to_leaf(prev_node)
                if leaf[1] == 0:
                    leaf[0].setLeft(new_node)
                else:
                    leaf[0].setRight(new_node)
                new_node.setParent(leaf[0])
            cnt_rebalanced = self.balance_all_the_way_up(new_node)
        self.size += 1
        return cnt_rebalanced

    def path_to_leaf(self, node: AVLNode):
        if not node.getLeft().isRealNode():
            return node, 0
        p = node.getLeft()
        while p.getRight().isRealNode():
            p = p.getRight()
        return p, 1

    def test_insert_and_delete(self, node: AVLNode):
        assert node.isRealNode()
        assert not node.getLeft().isRealNode()
        assert not node.getRight().isRealNode()
        while node.getParent() is not None:
            assert node.getSize() == 1 + node.getLeft().getSize() + node.getRight().getSize()
            assert node.getHeight() == 1 + max(node.getLeft().getHeight(), node.getRight().getHeight())
            node = node.getParent()

    """deletes the i'th item in the list
    
    @type i: int
    @pre: 0 <= i < self.length()
    @param i: The intended index in the list to be deleted
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    def delete(self, i):
        if 0 > i or i >= self.length():
            return -1
        node_to_delete = self.retrieveNode(i)
        parent = node_to_delete.getParent()
        if self.firstNode is node_to_delete:
            self.firstNode = self.successor(node_to_delete)
        if self.lastNode is node_to_delete:
            self.lastNode = self.predecessor(node_to_delete)
        rel_to_parent = node_to_delete.relationToParent()
        cnt_rebalanced = 0
        # node is leaf
        if node_to_delete.isLeaf():
            if rel_to_parent == "root":
                self.root = None
                self.size = 0
                return 0
            # requested to delete the root, and it is a leaf
            elif rel_to_parent == "left":
                parent.place_virtual_nodes_on_leaf("left")
            else:
                parent.place_virtual_nodes_on_leaf("right")
            parent.resetHeight()
            parent.resetSize()
        elif node_to_delete.getRight().isRealNode() and node_to_delete.getLeft().isRealNode():  # node has 2 sons
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
        elif not node_to_delete.getRight().isRealNode():  # node has only left son
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
        else:  # node has only right son
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

        cnt_rebalanced += self.balance_all_the_way_up(parent)
        self.size -= 1
        return cnt_rebalanced

    """returns the value of the first item in the list
    
    @rtype: str
    @returns: the value of the first item, None if the list is empty
    """

    def first(self):
        if self.empty():
            return None
        return self.firstNode.getValue()

    """returns the value of the last item in the list
    
    @rtype: str
    @returns: the value of the last item, None if the list is empty
    """

    def last(self):
        if self.empty():
            return None
        return self.lastNode.getValue()

    """returns an array representing list 
    
    @rtype: list
    @returns: a list of strings representing the data structure
    """

    def listToArray(self) -> list:
        return self.listToArrayRec(self.root)

    def listToArrayRec(self, node) -> list:
        if not node.isRealNode():
            return []
        result = self.listToArrayRec(node.getLeft())
        result.append(node.value)
        result.extend(self.listToArrayRec(node.getRight()))
        return result

    def getSize(self):
        return self.size

    """returns the size of the list 
    
    @rtype: int
    @returns: the size of the list
    """

    def getTreeHeight(self):
        return self.root.getHeight()

    def length(self):
        return self.size

    """sort the info values of the list
    
    @rtype: list
    @returns: an AVLTreeList where the values are sorted by the info of the original list.
    """
    """"""

    def sort(self):
        arr = self.listToArray()
        arr, cnt_nones = self.relocate_nones_to_the_end(arr)
        arr = self.merge_sorted(arr, 0, len(arr) - cnt_nones - 1)
        arr.extend([None for i in range(cnt_nones)])
        result = self.build_tree_from_array(arr)
        self.balance_if_needed(result.root)
        return result

    """
    Sort the given array using the merge sort algorithm.

    @pre: The array is not empty.

    @post: The array is sorted in ascending order.
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

    @pre: The array is not empty.

    @post: None values are at the end of the array.
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
    """

    def permutation(self):
        array_tree = self.listToArray()
        array_result = []
        len_result = len(array_tree)
        for _ in range(len_result):
            index = random.randrange(0, len(array_tree))
            array_result.append(array_tree[index])
            array_tree[index], array_tree[-1] = array_tree[-1], array_tree[index]
            array_tree.pop()
        result = self.build_tree_from_array(array_result)
        self.balance_if_needed(result.root)
        return result

    def build_tree_from_array(self, array: list):
        result = AVLTreeList()
        if len(array) == 0:
            return result
        result.root = AVLNode(array[len(array)//2])
        self.build_tree_from_array_rec(result.root, array, 0, len(array) - 1)
        result.size = result.root.size
        result.first = result.retrieveNode(0)
        result.last = result.retrieveNode(result.size - 1)
        return result

    def build_tree_from_array_rec(self, node: AVLNode, array: list, i, j):
        mid = (i + j) // 2
        node.setValue(array[mid])
        if mid == i:
            virtual_node = AVLNode("")
            virtual_node.setParent(node)
            virtual_node.setHeight(-1)
            virtual_node.setSize(0)
            node.setLeft(virtual_node)
        else:
            left = AVLNode("place holder")
            node.setLeft(left)
            left.setParent(node)
            self.build_tree_from_array_rec(left, array, i, mid - 1)
            left.resetSize()
            left.resetHeight()
        if mid == j:
            virtual_node = AVLNode("")
            virtual_node.setParent(node)
            virtual_node.setHeight(-1)
            virtual_node.setSize(0)
            node.setRight(virtual_node)
        else:
            right = AVLNode("place holder")
            node.setRight(right)
            right.setParent(node)
            self.build_tree_from_array_rec(right, array, mid + 1, j)
            right.resetSize()
            right.resetHeight()
        node.resetSize()
        node.resetHeight()

    def balance_if_needed(self, node: AVLNode):
        if not node.isRealNode():
            return
        self.balance_if_needed(node.getLeft())
        self.balance_if_needed(node.getRight())
        if abs(node.getBF()) > 1:
            self.balance_all_the_way_up(node)

    def copy_tree(self):
        new_tree = AVLTreeList()
        if self.empty():
            return new_tree
        new_tree.root = AVLNode(self.root.getValue())
        self.copy_tree_rec(self.root, new_tree.root)
        new_tree.size = new_tree.getSize()
        new_tree.first = new_tree.retrieveNode(0)
        new_tree.last = new_tree.retrieveNode(new_tree.size - 1)
        return new_tree

    def copy_tree_rec(self, old_node: AVLNode, new_node: AVLNode):
        new_node.setValue(old_node.getValue())
        if old_node.getLeft().isRealNode():
            left = AVLNode(old_node.getLeft().getValue())
            new_node.setLeft(left)
            left.setParent(new_node)
            self.copy_tree_rec(old_node.getLeft(), left)
            left.resetSize()
            left.resetHeight()
        else:
            virtual_node = AVLNode("")
            virtual_node.setParent(new_node)
            virtual_node.setHeight(-1)
            virtual_node.setSize(0)
            new_node.setLeft(virtual_node)
        if old_node.getRight().isRealNode():
            right = AVLNode(old_node.getRight().getValue())
            new_node.setRight(right)
            right.setParent(new_node)
            self.copy_tree_rec(old_node.getRight(), right)
            right.resetSize()
            right.resetHeight()
        else:
            virtual_node = AVLNode("")
            virtual_node.setParent(new_node)
            virtual_node.setHeight(-1)
            virtual_node.setSize(0)
            new_node.setRight(virtual_node)
        new_node.resetSize()
        new_node.resetHeight()

    """concatenates lst to self
    
    @type lst: AVLTreeList
    @param lst: a list to be concatenated after self
    @rtype: int
    @returns: the absolute value of the difference between the height of the AVL trees joined
    """

    def concat(self, lst):
        lst: AVLTreeList
        # resolve all edge cases
        if self.empty() and lst.empty():
            return 0
        if self.empty():
            self.root = lst.root
            self.firstNode = lst.firstNode
            self.lastNode = lst.lastNode
            self.size = lst.size
            return lst.root.getHeight() + 1
        if lst.empty():
            return self.root.getHeight() + 1
        if self.size == 1:
            lst.insert(0, self.root.getValue())
            self.root = lst.root
            self.firstNode = lst.firstNode
            self.lastNode = lst.lastNode
            self.size = lst.size
            return lst.root.getHeight() - 1
        dif = abs(self.root.getHeight() - lst.root.getHeight())  # the return value
        # concat lst after self. use self's last as the connecting node
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
        """

    def search(self, val):
        if self.root == None:
            return -1
        node = self.search_node_rec(self.root, val)
        if node is None:
            return -1
        else:
            return self.get_node_index(node)

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
   @pre: node is a valid AVLNode instance belonging to the AVL tree.
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

    """returns the root of the tree representing the list
    
    @rtype: AVLNode
    @returns: the root, None if the list is empty
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


    def getRoot(self):
        return self.root

    def retrieveNode(self, i) -> AVLNode:
        return self.retrieveNodeRec(self.root, i)

    def retrieveNodeRec(self, currentNode, i):
        if currentNode.getLeft().getSize() == i:
            return currentNode
        elif currentNode.getLeft().getSize() > i:
            return self.retrieveNodeRec(currentNode.getLeft(), i)
        return self.retrieveNodeRec(currentNode.getRight(), i - (currentNode.getLeft().getSize() + 1))

    def balance_all_the_way_up(self, node: AVLNode) -> int:
        cnt_rebalanced = 0
        while node is not None:
            node.resetSize()
            node.resetHeight()
            node_BF = node.getBF()
            # rotation if needed
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
            node = node.getParent()
        return cnt_rebalanced

    def replace_nodes(self, node1: AVLNode, node2: AVLNode):
        tmp_value = node1.getValue()
        node1.setValue(node2.getValue())
        node2.setValue(tmp_value)


    def append(self, val):
        self.insert(self.length(), val)



def test2():
    twentyTree = AVLTreeList()

    for i in range(20):
        twentyTree.append(i)
    twentyTree.delete(3)
    twentyTree.delete(3)
    twentyTree.delete(4)
    twentyTree.delete(2)
    print(twentyTree.first())


if __name__ == "__main__":
    test2()
