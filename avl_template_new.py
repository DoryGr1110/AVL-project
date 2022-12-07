# username - complete info
# id1      - complete info
# name1    - complete info
# id2      - complete info
# name2    - complete info


"""A class represnting a node in an AVL tree"""


class AVLNode(object):
    """Constructor, you are allowed to add more fields.

	@type value: str
	@param value: data of your node
	"""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = -1  # Balance factor
        self.size = 0

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

    def relationToParent(self):
        if self.getParent() is None:
            return "root"
        return "left" if self.getParent().getLeft() == self  else "right"

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
            if relToPar != "root":
                y.setParent(parent)
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
            if relToPar != "root":
                y.setParent(parent)
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

    """returns whether the list is empty

	@rtype: bool
	@returns: True if the list is empty, False otherwise
	"""

    def empty(self):
        return None

    """retrieves the value of the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: index in the list
	@rtype: str
	@returns: the the value of the i'th item in the list
	"""

    def retrieve(self, i):
        return self.retrieveNode(i).getValue

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
        return -1

    """deletes the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list to be deleted
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""

    def delete(self, i):
        return -1

    """returns the value of the first item in the list

	@rtype: str
	@returns: the value of the first item, None if the list is empty
	"""

    def first(self):
        return None

    """returns the value of the last item in the list

	@rtype: str
	@returns: the value of the last item, None if the list is empty
	"""

    def last(self):
        return None

    """returns an array representing list 

	@rtype: list
	@returns: a list of strings representing the data structure
	"""

    def listToArray(self):
        return None

    """returns the size of the list 

	@rtype: int
	@returns: the size of the list
	"""

    def length(self):
        return None

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
        return None

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

    def getRoot(self):
        return None

    def retrieveNode(self, i):
        return retrieveNodeRec(self.root, i)

    def retrieveNodeRec(self, currentNode, i):
        if currentNode.getLeft().getSize() == i - 1:
            return currentNode
        elif currentNode.getLeft().getSize() > i:
            return retrieveNodeRec(self, currentNode.getLeft(), i)
        return retrieveNodeRec(self, currentNode.getRight(), i - (currentNode.getLeft().getSize() + 1))


