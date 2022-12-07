#username - complete info
#id1      - complete info
#name1    - complete info
#id2      - complete info
#name2    - complete info



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
		self.height = -1 # Balance factor
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

	"""returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""
	def isRealNode(self):
		return self.height != -1

	def resetHeight(self):
		self.height = 1 + max(self.getRight().getHeight(), self.getLeft().getHeight())

	def resetSize(self):
		self.size = self.getRight().getSize() + self.getLeft().getSize() + 1



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
		return None

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
		if self.empty():
			return None
		return self.first().getValue()


	"""returns the value of the last item in the list

	@rtype: str
	@returns: the value of the last item, None if the list is empty
	"""
	def last(self):
		if self.empty():
			return None
		return self.last().getValue()

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

	tree = AVLTreeList()
	tree.root = rootd
	tree.size = 5

	if (tree.retrieve(2) != "c" or tree.retrieve(4) != "e"):
		print("***error in retrieve method***")

	rootd.rotate("right")

	if (secondRightc.getParent() != rootd or
			rootd.getLeft() != secondRightc or
			rootd.getParent() != firstLeftb or
			firstLeftb.getRight() != rootd or
			firstLeftb.getParent() != None or
			firstLeftb.getHeight() != 2 or
			rootd.getHeight() != 1):
		print("***error in rotate method***")

	rootd.rotate("right")

	if (firstRighte.getParent() != rootd or
			rootd.getRight() != firstRighte or
			rootd.getParent() != secondRightc or
			secondRightc.getRight() != rootd or
			secondRightc.getParent() != firstLeftb or
			secondRightc.getHeight() != 2 or
			firstRighte.getHeight() != 0 or
			rootd.getHeight() != 1):
		print("***error in rotate method***")

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
    test()
