class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

"""
                           20
                15                  30
            10      18          25      45
        5       7            24   28

"""

# Set up tree:
tree = BinaryTree(20)
tree.root.left = Node(15)
tree.root.right = Node(30)
tree.root.left.left = Node(10)
tree.root.left.right = Node(18)
tree.root.left.left.left = Node(5)
tree.root.left.left.right = Node(7)
tree.root.right.left = Node(25)
tree.root.right.right = Node(45)
tree.root.right.left.left = Node(24)
tree.root.right.left.right = Node(28)

def depth_first_traversal_recursive_preorder(root):
    if not root:
        return
    print(root.val)
    depth_first_traversal_recursive_preorder(root.left)
    depth_first_traversal_recursive_preorder(root.right)

def depth_first_traversal_iterative_preorder(root):
    stack = [root]
    while stack:
        node = stack.pop()
        print(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

def depth_first_traversal_recursive_postorder(root):
    if not root:
        return
    depth_first_traversal_recursive_inorder(root.left)
    depth_first_traversal_recursive_inorder(root.right)
    print(root.val)

def depth_first_traversal_iterative_postorder(root):
        if not root:
            return
        result = []
        stack = [root]
        while stack:
            node = stack.pop()
            if not node.left and not node.right:
                result.append(node.val)
            else:
                stack.append(node)
                if node.right:
                    stack.append(node.right)
                    node.right = None
                if node.left:
                    stack.append(node.left)
                    node.left = None
        return result

depth_first_traversal_iterative_inorder(tree.root)