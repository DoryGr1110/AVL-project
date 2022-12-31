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
        if (0 > i or i >= self.length()):
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
            return (node, 0)
        p = node.getLeft()
        while p.getRight().isRealNode():
            p = p.getRight()
        return (p, 1)

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
        if (0 > i or i >= self.length()):
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

    def listToArray(self):
        return self.listToArrayRec(self.root)

    def listToArrayRec(self, node):
        if not node.isRealNode():
            return []
        return self.listToArrayRec(node.getLeft()) + [node.value] + self.listToArrayRec(node.getRight())

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
        lst: AVLTreeList
        # resolve all edge cases
        if self.empty() and lst.empty():
            return 0
        if self.empty():
            self.root = lst.root
            self.firstNode = lst.firstNode
            self.lastNode = lst.lastNode
            self.size = lst.size
            return lst.root.getHeight()
        if lst.empty():
            return self.root.getHeight()
        if self.size == 1:
            lst.insert(0, self.root.getValue())
            self.root = lst.root
            self.firstNode = lst.firstNode
            self.lastNode = lst.lastNode
            self.size = lst.size
            return lst.root.getHeight() - 1
        dif = abs(self.root.getHeight() - lst.root.getHeight())  # the return value
        # concat lst after self. use self's last as the connecting node
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
        connecting_node.setRight(p_self)
        connecting_node.setLeft(p_lst)
        if parent_node_tree is None:
            connecting_node.setParent(None)
            self.root = connecting_node
        elif parent_node_tree == self:
            connecting_node.setParent(p_self.getParent())
            p_self.getParent().setRight(connecting_node)
        elif parent_node_tree == lst:
            connecting_node.setParent(p_lst.getParent())
            p_lst.getParent().setLeft(connecting_node)
        connecting_node.resetSize()
        connecting_node.resetHeight()
        self.size += lst.getSize()
        self.balance_all_the_way_up(connecting_node)
        return dif

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

def test():
    rootd = AVLNode("d")
    firstLeftb = AVLNode("b")
    firstRighte = AVLNode("e")
    secondLefta = AVLNode("a")
    secondRightc = AVLNode("c")

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

    tree.rotate("right", rootd)

    if (secondRightc.getParent() != rootd or
            rootd.getLeft() != secondRightc or
            rootd.getParent() != firstLeftb or
            firstLeftb.getRight() != rootd or
            firstLeftb.getParent() != None or
            firstLeftb.getHeight() != 2 or
            rootd.getHeight() != 1):
        print("***error in rotate method1***")

    tree.rotate("right", rootd)

    if (firstRighte.getParent() != rootd or
            rootd.getRight() != firstRighte or
            rootd.getParent() != secondRightc or
            secondRightc.getRight() != rootd or
            secondRightc.getParent() != firstLeftb or
            secondRightc.getHeight() != 2 or
            firstRighte.getHeight() != 0 or
            rootd.getHeight() != 1):
        print("***error in rotate method2***")

    tree.rotate("left", secondRightc)

    if (secondRightc.getParent() != rootd or
            rootd.getLeft() != secondRightc or
            rootd.getParent() != firstLeftb or
            firstLeftb.getRight() != rootd or
            firstLeftb.getParent() != None or
            firstLeftb.getHeight() != 2 or
            rootd.getHeight() != 1):
        print("***error in rotate method***")

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
    # test()
    test2()
