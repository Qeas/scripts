class TreeNode(object):
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

"""
				15
		10					25
	5		7			20		35
							30		40

"""


class Solution():
	def inorder_successor(self, root, n):
		if not root:
			return
		while root:
			candidate = root
			if root.val == n:
				return root.right if root.right else root
			if n > root.val:
				root = root.right
			else:
				root = root.left
		return candidate

root = TreeNode(15)
root.right = TreeNode(25)
root.right.right = TreeNode(35)
root.right.left = TreeNode(20)
root.right.right.right = TreeNode(40)
root.right.right.left = TreeNode(30)
root.left = TreeNode(10)
root.left.left = TreeNode(5)
root.left.right = TreeNode(7)

s = Solution()
print(s.inorder_successor(root, 1).val)
