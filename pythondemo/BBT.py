class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


def insert(root, newValue):
    # if binary search tree is empty, make a new node and declare it as root
    if root is None:
        root = BinaryTreeNode(newValue)
        return root
    # binary search tree is not empty, so we will insert it into the tree
    # if newValue is less than value of data in root, add it to left subtree and proceed recursively
    if newValue < root.data:
        root.leftChild = insert(root.leftChild, newValue)
    else:
        # if newValue is greater than value of data in root, add it to right subtree and proceed recursively
        root.rightChild = insert(root.rightChild, newValue)
    return root


def height(root):
    # if root is None return 0
    if root == None:
        return 0
    # find height of left subtree
    hleft = height(root.leftChild)
    # find the height of right subtree
    hright = height(root.rightChild)
    # find max of hleft and hright, add 1 to it and return the value
    if hleft > hright:
        return hleft + 1
    else:
        return hright + 1


root = insert(None, 15)
insert(root, 10)
insert(root, 25)
insert(root, 6)
insert(root, 14)
insert(root, 20)
insert(root, 60)
print("Printing the height of the binary tree.")
print(height(root))