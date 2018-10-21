# Reverse level travesal of binary tree
from collections import deque

class Node(object):
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
		
	def __str__(self):
		return "{0}-[{1}]-{2}".format(str(self.left), str(self.val), str(self.right))
	

def reverse_order(root):
	queue = deque()
	stack = []
	
	if root:
		queue.append(root)

	while queue:
		cur = queue.popleft()
		stack.append(cur.val)
		if cur.right:
			queue.append(cur.right)
		if cur.left:
			queue.append(cur.left)
	
	print '-'.join(str(val) for val in stack[::-1])

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
reverse_order(root)