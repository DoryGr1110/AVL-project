# username - complete info
# id1      - complete info
# name1    - complete info
# id2      - complete info
# name2    - complete info



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
        return self.getRight().getHeight() - self.getLeft().getHeight()

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

	def relationToParent(self):
		if self.getParent() is None:
			return "root"
		return "left" if self.getParent().getLeft() == self else "right"

	def rotate(self, side):
		x = self
		if side == "right":
			parent = x.getParent()
			relToPar = x.relationToParent()
			y = x.getLeft()
			x.setLeft(y.getRight())
			x.getLeft().setParent(x)
			y.setRight(x)
			x.setParent(y)
			y.setParent(parent)
			if relToPar != "root":
				if relToPar == "right":
					parent.setRight(y)
				else:
					parent.setLeft(y)
		else:
			parent = x.getParent()
			relToPar = x.relationToParent()
			y = x.getRight()
			x.setRight(y.getLeft())
			x.getRight().setParent(x)
			y.setLeft(x)
			x.setParent(y)
			y.setParent(parent)
			if relToPar != "root":
				if relToPar == "right":
					parent.setRight(y)
				else:
					parent.setLeft(y)
		x.resetSize()
		x.resetHeight()
		y.resetSize()
		y.resetHeight()
		if relToPar != "root":
			parent.resetSize()
			parent.resetHeight()

    def setSize(self, size):
        self.size = size

    def place_virtual_nodes_on_leaf(self):
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


"""
A class implementing the ADT list, using an AVL tree.
"""


class AVLTreeList(object):
    """
    Constructor, you are allowed to add more fields.
    """

    def __init__(self):
        self.size = 0
        self.root = None
        # add your fields here
        self.first = None
        self.last = None


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
        return self.retrieveNode(i).getValue()

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
        new_node = AVLNode(val)
        if i == 0:
            self.first = new_node
        prev_node = self.retrieveNode(i)
        prev_node.setLeft(new_node)
        new_node.setParent(prev_node)
        new_node.place_virtual_nodes_on_leaf()
        cnt_rebalanced = self.balance_all_the_way_up(new_node)
        self.test_insert_and_delete(new_node)
        return cnt_rebalanced


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
        node_to_delete = self.retrieveNode(i)
        parent = node_to_delete.getParent()
        if self.first() == node_to_delete:
            self.first = parent
        if self.last() == node_to_delete:
            self.last = parent
        rel_to_parent = node_to_delete.relationToParent()
        cnt_rebalanced = 0
        # node is leaf
        if node_to_delete.isLeaf():
            if rel_to_parent == "root":
                self.root = None
            # requested to delete the root, and it is a leaf
            else:
                parent.place_virtual_nodes_on_leaf()
        elif node_to_delete.getRight() is not None and node_to_delete.getLeft() is not None:  # node has 2 sons
            successor = self.successor(node_to_delete)
            self.replace_nodes(node_to_delete, successor)
            parent = node_to_delete.getParent()
            if rel_to_parent == "right":
                parent.setRight(None)
            else:
                parent.setLeft(None)
        elif node_to_delete.getRight() is None:    # node has 1 son
            if rel_to_parent == "left":
                parent.setLeft(node_to_delete.getRight())
                parent.getLeft().setParent(parent)
            elif rel_to_parent == "right":
                parent.setRight(node_to_delete.getRight())
                parent.getRight().setParent(parent)
        elif node_to_delete.getLeft() is None:
            if rel_to_parent == "left":
                parent.setLeft(node_to_delete.getLeft())
                parent.getLeft().setParent(parent)
            elif rel_to_parent == "right":
                parent.setRight(node_to_delete.getLeft())
                parent.getRight().setParent(parent)

        parent.resetHeight()
        parent.resetSize()

        cnt_rebalanced += self.balance_all_the_way_up(parent)
        self.test_insert_and_delete(parent)
        return cnt_rebalanced

    """returns the value of the first item in the list
    
    @rtype: str
    @returns: the value of the first item, None if the list is empty
    """

    def first(self):
        if self.empty():
            return None
        return self.first.getValue()


    """returns the value of the last item in the list
    
    @rtype: str
    @returns: the value of the last item, None if the list is empty
    """

    def last(self):
        if self.empty():
            return None
        return self.last.getValue()

    """returns an array representing list 
    
    @rtype: list
    @returns: a list of strings representing the data structure
    """

    def listToArray(self):
        return self.listToArrayRec(self.root)

    def listToArrayRec(self, node):
        if not node.isRealNode():
            return []
        return self.listToArrayRec(node.getLeft()) + [node.value] + self.listToArrayRec(node.getRight())


    """returns the size of the list 
    
    @rtype: int
    @returns: the size of the list
    """

    def length(self):
        return self.size

    """sort the info values of the list
    
    @rtype: list
    @returns: an AVLTreeList where the values are sorted by the info of the original list.
    """

    def sort(self):
        return None

    """permute the info values of the list 
    
    @rtype: list
    @returns: an AVLTreeList where the values are permuted randomly by the info of the original list. ##Use Randomness
    """

    def permutation(self):
        new_tree = self.copyTree(self.getRoot())


	def copyTree(self, root):
		new_node = AVLNode(root.getValue())

		left_child = self.copyTree(root.getLeft())
		right_child = self.copyTree(root.getRight())

		new_node.setLeft(left_child)
		new_node.setRight(right_child)

		left_child.setParent(new_node)
		right_child.setParent(new_node)

		return new_node


    """concatenates lst to self
    
    @type lst: AVLTreeList
    @param lst: a list to be concatenated after self
    @rtype: int
    @returns: the absolute value of the difference between the height of the AVL trees joined
    """

    def concat(self, lst):
        return None

    """searches for a *value* in the list
    
    @type val: str
    @param val: a value to be searched
    @rtype: int
    @returns: the first index that contains val, -1 if not found.
    """

    def search(self, val):
        return None

    """returns the root of the tree representing the list
    
    @rtype: AVLNode
    @returns: the root, None if the list is empty
    """

    def successor(self, node):
        if node is self.last:
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


    def getRoot(self):
        return self.root

    def retrieveNode(self, i) -> AVLNode:
        return self.retrieveNodeRec(self.root, i)

    def retrieveNodeRec(self, currentNode, i):
        if currentNode.getLeft().getSize() == i - 1:
            return currentNode
        elif currentNode.getLeft().getSize() > i:
            return self.retrieveNodeRec(currentNode.getLeft(), i)
        return self.retrieveNodeRec(currentNode.getRight(), i - (currentNode.getLeft().getSize() + 1))

    def balance_all_the_way_up(self, node: AVLNode) -> int:
        cnt_rebalanced = 0
        while node.getParent() is not None:
            node.resetSize()
            node.resetHeight()
            parent = node.getParent()
            parent.resetHeight()
            parent.resetSize()
            node_BF = node.getBF()
            parent_BF = parent.getBF()
            # rotation if needed
            if parent_BF <= -2 and node_BF <= 0:
                parent.rotate("left")
                cnt_rebalanced += 1
            elif parent_BF <= -2 and node_BF >= 1:
                node.rotate("right")
                parent.rotate("left")
                cnt_rebalanced += 2
                node = parent
            elif parent_BF >= 2 and node_BF <= -1:
                node.rotate("left")
                parent.rotate("right")
                cnt_rebalanced += 2
                node = parent
            elif parent_BF >= 2 and node_BF >= 0:
                parent.rotate("right")
                cnt_rebalanced += 1
            else:
                node = parent
        return cnt_rebalanced


    def successor(self, node):
        return node

    def replace_nodes(self, node1: AVLNode, node2: AVLNode):
        node1.parent, node1.left, node1.right, node2.parent, node2.left, node2.right = node2.parent, node2.left, node2.right, node1.parent, node1.left, node1.right


def test():
    rootd = AVLNode("d")
    firstLeftb = AVLNode("b")
    firstRighte = AVLNode("e")
    secondLefta = AVLNode("a")
    secondRightc = AVLNode("a")

    rootd.setLeft(firstLeftb)
    firstLeftb.setParent(rootd)
    rootd.setRight(firstRighte)
    firstRighte.setParent(rootd)

    firstLeftb.setLeft(secondLefta)
    secondLefta.setParent(firstLeftb)
    firstLeftb.setRight(secondRightc)
    secondRightc.setParent(firstLeftb)

    virtual1 = AVLNode("virtual1")
    virtual2 = AVLNode("virtual2")
    virtual3 = AVLNode("virtual3")
    virtual4 = AVLNode("virtual4")
    virtual5 = AVLNode("virtual5")
    virtual6 = AVLNode("virtual6")

    virtual1.setParent(secondLefta)
    secondLefta.setLeft(virtual1)
    virtual2.setParent(secondLefta)
    secondLefta.setRight(virtual2)
    virtual3.setParent(secondRightc)
    secondRightc.setLeft(virtual3)
    virtual4.setParent(secondRightc)
    secondRightc.setRight(virtual4)
    virtual5.setParent(firstRighte)
    firstRighte.setLeft(virtual5)
    virtual6.setParent(firstRighte)
    firstRighte.setRight(virtual6)

    rootd.resetHeight()
    firstLeftb.resetHeight()
    firstRighte.resetHeight()
    secondLefta.resetHeight()
    secondRightc.resetHeight()

    secondRightc.resetSize()
    secondLefta.resetSize()
    firstRighte.resetSize()
    firstLeftb.resetSize()
    rootd.resetSize()

    tree = AVLTreeList()
    tree.root = rootd
    tree.size = 5

    if (tree.retrieve(1) != "b" or tree.retrieve(3) != "d"):
        print("***error in retrieve method***")

    rootd.rotate("right")

    if (secondRightc.getParent() != rootd or
            rootd.getLeft() != secondRightc or
            rootd.getParent() != firstLeftb or
            firstLeftb.getRight() != rootd or
            firstLeftb.getParent() != None or
            firstLeftb.getHeight() != 2 or
            rootd.getHeight() != 1):
        print("***error in rotate method1***")

    rootd.rotate("right")

    if (firstRighte.getParent() != rootd or
            rootd.getRight() != firstRighte or
            rootd.getParent() != secondRightc or
            secondRightc.getRight() != rootd or
            secondRightc.getParent() != firstLeftb or
            secondRightc.getHeight() != 2 or
            firstRighte.getHeight() != 0 or
            rootd.getHeight() != 1):
        print("***error in rotate method2***")

    secondRightc.rotate("left")

    if (secondRightc.getParent() != rootd or
            rootd.getLeft() != secondRightc or
            rootd.getParent() != firstLeftb or
            firstLeftb.getRight() != rootd or
            firstLeftb.getParent() != None or
            firstLeftb.getHeight() != 2 or
            rootd.getHeight() != 1):
        print("***error in rotate method***")

if __name__ == "__main__":
    # test1()
    # test2()
    # test3()
    print()


