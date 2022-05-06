# 
# A Binary Search Tree (BST) is a sorted hierarchical data structure,
# in which each of the nodes has has at most two children and follows the below-mentioned properties :
#       -> The value of the key of the left sub-tree is less than the value of its parent (root) node's key.
#       -> The value of the key of the right sub-tree is greater than or equal to the value of its parent (root) node's key.
#
# How many structurally unique BSTs for keys from 1..N?
# Given a list of n distinct numbers, we are interested in computing the number of BSTs labeled by these numbers. 
# Without the loss of generality, we can assume the numbers are 1, 2, 3, ..., n. 
# For example, there are 5 possible BSTs for 1, 2, 3:
#
#
#
# Binary Tree Node
""" A utility function to create a
new BST node """
class newNode:
    # Construct to create a newNode
    def __init__(self, item):
        self.key=item
        self.left = None
        self.right = None

# A utility function to do inorder traversal of BS
def inorder(root):
    if root is not None:
        # Traverse left
        inorder(root.left)
        # Traverse root
        print(str(root.key), end=' ')
        # Traverse right
        inorder(root.right)
 
# A utility function to do preorder traversal of BST
def preorder(root) :
 
    if (root != None) :
     
        print(root.key, end = " " )
        preorder(root.left)
        preorder(root.right)


# Insert a node
def insert(node, key):

    # Return a new node if the tree is empty
    if node is None:
        return newNode(key)

    # Traverse to the right place and insert the node
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    return node

# Find the inorder successor
def minValueNode(node):
    current = node

    # Find the leftmost leaf
    while(current.left is not None):
        current = current.left

    return current


# Deleting a node
def deleteNode(root, key):

    # Return if the tree is empty
    if root is None:
        return root

    # Find the node to be deleted
    if key < root.key:
        root.left = deleteNode(root.left, key)
    elif(key > root.key):
        root.right = deleteNode(root.right, key)
    else:
        # If the node is with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # If the node has two children,
        # place the inorder successor in position of the node to be deleted
        temp = minValueNode(root.right)

        root.key = temp.key

        # Delete the inorder successor
        root.right = deleteNode(root.right, temp.key)

    return root


# function for constructing trees
def constructTrees(start, end):
 
    list = []
 
    """ if start > end then subtree will be
        empty so returning None in the list """
    if (start > end) :
     
        list.append(None)
        return list
     
    """ iterating through all values from
        start to end for constructing
        left and right subtree recursively """
    for i in range(start, end + 1):
     
        """ constructing left subtree """
        leftSubtree = constructTrees(start, i - 1)
 
        """ constructing right subtree """
        rightSubtree = constructTrees(i + 1, end)
 
        """ now looping through all left and
            right subtrees and connecting
            them to ith root below """
        for j in range(len(leftSubtree)) :
            left = leftSubtree[j]
            for k in range(len(rightSubtree)):
                right = rightSubtree[k]
                node = newNode(i)   # making value i as root
                node.left = left    # connect left subtree
                node.right = right    # connect right subtree
                list.append(node)    # add this tree to list
    return list


def numBST(nodeValues):
    trees_from_1_to_n = constructTrees(1,nodeValues)
    print("Total possible BSTs from",1,"to",nodeValues,"is : ", len(trees_from_1_to_n))
    return(trees_from_1_to_n)


# Driver Code
if __name__ == '__main__':
 
    # Construct all possible BSTs
    bsts = numBST(3)
    """ Printing inorder traversal of all constructed BSTs """
    print("Inorder traversals of all",
                "constructed BSTs are")
    for i in range(len(bsts)):
        inorder(bsts[i])
        print()
    
    print("\n========\n")

    """ Printing preorder traversal of all constructed BSTs """
    print("Preorder traversals of all",
                "constructed BSTs are")
    for i in range(len(bsts)):
        preorder(bsts[i])
        print()