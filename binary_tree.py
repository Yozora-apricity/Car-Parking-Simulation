class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def ltr(node): # In-order
    if not node: return []
    return ltr(node.left) + [node.value] + ltr(node.right)

def tlr(node):
    if not node: return []
    return [node.value] + tlr(node.left) + tlr(node.right)

def lrt(node):
    if not node: return []
    return lrt(node.left) + lrt(node.right) + [node.value]