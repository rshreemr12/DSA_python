class Node:
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None

class Tree:
    """
    should have 1 root node 
    each node can have any number of child node
    each node links to only 1 node
    node cannot be its own parent
    """
    def __init__(self, root, name=''):
        self.root = root
        self.name = name


# root node
node = Node(2)

node.left = Node(3)
node.left.left = Node(1)

node.right = Node(5)
node.right.left = Node(3)
node.right.left.right = Node(4)

node.right.right = Node(7)
node.right.right.left = Node(6)
node.right.right.right = Node(8)

tree = Tree(node, "big tree")


# node = Node(10)

# node.left = Node(5)
# node.right = Node(15)

# node.left.left = Node(2)
# node.left.right = Node(6)

# node.right.left = Node(13)
# node.right.right = Node(10000)

# myTree = Tree(node, 'Ramya\'s Tree')

print(tree.name)
print(tree.root.left.data)

print(tree.root.right.right.data)     