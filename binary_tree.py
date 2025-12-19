# BINARY TREE LOGIC
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def ltr(node): # In-order
    if not node: return []
    return ltr(node.left) + [node.value] + ltr(node.right)

def tlr(node): # Pre-order
    if not node: return []
    return [node.value] + tlr(node.left) + tlr(node.right)

def lrt(node): # Post-Order
    if not node: return []
    return lrt(node.left) + lrt(node.right) + [node.value]

class BinaryTreeOrder:
    def __init__(self):
        self.root = None

    def tree_level_order(self, values):
        if not values:
            self.root = None
            return

        self.root = BinaryTreeNode(values[0])
        next_node_value = [self.root]
        node_index = 1

        while next_node_value and node_index < len(values):
            node = next_node_value.pop(0)

            if node_index < len(values):
                node.left = BinaryTreeNode(values[node_index])
                next_node_value.append(node.left)
                node_index += 1

            if node_index < len(values):
                node.right = BinaryTreeNode(values[node_index])
                next_node_value.append(node.right)
                node_index += 1