# Reverse level travesal of binary tree
from collections import deque

class Node(object):
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
		
	def __str__(self):
		return "{0}-[{1}]-{2}".format(str(self.left), str(self.val), str(self.right))
	

def in_order(root):
	queue = deque()
	if root:
		queue.append(root)

	while queue:
		cur = queue.popleft()
		if cur.left:
			queue.append(cur.left)
		if cur.right:
			queue.append(cur.right)
		yield str(cur.val)

	
def to_balanced(root):
	queue = deque()
	arr = []
	if root:
		queue.append(root)
	while queue:
		curr = queue.popleft()
		arr.append(curr.val)
		if curr.left:
			queue.append(curr.left)
		if curr.right:
			queue.append(curr.right)
	arr = sorted(arr)
	return arr_to_bt(arr, 0, len(arr)-1)

def arr_to_bt(arr, start, end):
	root = None
	if start > end:
		return root
	mid = (start + end)/2
	root = Node(mid)
	root.left = arr_to_bt(arr, start, mid-1)
	root.right = arr_to_bt(arr, mid+1, end)
	return root
		

root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.left.left = Node(5)
root.right = Node(3)

print '-'.join(in_order(root))
print '-'.join(in_order(to_balanced(root)))

