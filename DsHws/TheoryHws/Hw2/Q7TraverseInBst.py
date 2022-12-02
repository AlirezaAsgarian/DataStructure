class Node:
    value = 6
    left = None
    right = None

    def __init__(self, value):
        self.value = value


class bst:
    nodes = []

    def insert(self, node):
        if len(self.nodes) == 0:
            self.nodes.append(node)
            return
        self.insertIn(self.nodes[0], node)

    def insertIn(self, parent, node):
        if parent.value > node.value:
            if parent.left is None:
                parent.left = node
            else:
                self.insertIn(parent.left, node)
        else:
            if parent.right is None:
                parent.right = node
            else:
                self.insertIn(parent.right, node)

    def getRoot(self):
        return self.nodes[0]


def printPreOrder(root):
    if root is None : return
    print(root.value)
    printPreOrder(root.left)
    printPreOrder(root.right)


def printInOrder(node):
    if node is None : return
    printInOrder(node.left)
    print(node.value)
    printInOrder(node.right)


def printPostOrder(node):
    if node is None : return
    printPostOrder(node.left)
    printPostOrder(node.right)
    print(node.value)



def createTreeFromPreOrder(nodes,max,i):
    end = i + 1
    if nodes[i].value > nodes[i + 1].value :
        nodes[i].left = nodes[i + 1]
        end = createTreeFromPreOrder(nodes,nodes[i].value,i + 1)
    if nodes[end].value < max and end != len(nodes) :
        nodes[i].right = nodes[end]
        end = createTreeFromPreOrder(nodes,nodes[end].value , end + 1)
    return end
