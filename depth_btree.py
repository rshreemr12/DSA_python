class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def search(self, target):
        if self.data == target:
            print("Found it!")
            return self
        
        if self.left and self.data > target:
            return self.left.search(target)

        if self.right and self.data < target:
            return self.right.search(target)

        print("Value is not in tree")

    def getNodesAtDepth(self, depth, nodes=[]):
        if depth == 0:
            nodes.append(self.data)
            return nodes

        if self.left:
            self.left.getNodesAtDepth(depth-1, nodes)
        else:
            nodes.extend([None]*2**(depth-1))
        
        if self.right:
            self.right.getNodesAtDepth(depth-1, nodes)
        else:
            nodes.extend([None]*2**(depth-1))
        return nodes

    def height(self, h=0):
        leftHeight = self.left.height(h+1) if self.left else h 
        rightHeight = self.right.height(h+1) if self.right else h
        return max(leftHeight, rightHeight)

class Tree:
    def __init__(self, root, name=''):
        self.root = root
        self.name = name

    def search(self, target):
        return self.root.search(target)
    
    def getNodesAtDepth(self, depth):
        return self.root.getNodesAtDepth(depth)

    def height(self):
        return self.root.height()

# tree = Tree(Node(50), 'A Very Tall Tree')
# tree.root.left = Node(25)
# tree.root.right = Node(75)
# tree.root.left.left = Node(10)
# tree.root.left.right = Node(35)
# tree.root.left.right.left = Node(30)
# tree.root.left.right.right = Node(42)
# tree.root.left.left.left = Node(5)
# tree.root.left.left.right = Node(13)
# tree.root.left.left.left.left = Node(2)


tree = Tree(Node(50))
tree.root.left = Node(25)
tree.root.right = Node(75)
tree.root.left.left = Node(13)
tree.root.left.right = Node(35)
tree.root.left.right.right = Node(37)
tree.root.right.left = Node(55)
tree.root.right.right = Node(103)
tree.root.left.left.left = Node(2)
tree.root.left.left.right = Node(20)
tree.root.right.left = Node(55)
tree.root.right.right.right = Node(256)

print(tree.height())

# tree = Tree(Node(50), 'A Very Short Tree')
print(tree.height())

print(tree.getNodesAtDepth(3))
