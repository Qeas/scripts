class Node(object):
	def __init__(self, val, next=None):
		self.val = val
		self.next = next
		self.prev_max = None

class Stack(object):
	def __init__(self, val):
		head = Node(val)
		self.head = head
		self.max = head

	def push(self, val):
		node = Node(val)
		if node.val > self.max.val:
			node.prev_max = self.max
			self.max = node
		node.next = self.head
		self.head = node

	def pop(self):
		if self.head == self.max:
			self.max = self.head.prev_max
		self.head = self.head.next

s = Stack(1)
s.push(3)
s.push(5)
s.push(2)
s.push(6)
s.push(4)
s.pop()
s.pop()
s.pop()
print s.max.val