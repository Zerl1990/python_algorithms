# Red black tree: Self balancing tree
# Every node has the following rules:
#   1) Root Property: The root is black
#   2) External Property: Every extarnal node is black -> None pointer
#   3) Red Property: The children of a red node are black
#   4) Depth Property: All external nodes have the same black height
#
# AVL vs Red Black: AVL is more balanced, so searching is faster but inserting is slower.
import os
import sys
import math

class Color:
	BLACK = 0
	RED = 1

class Node(object):
	def __init__(self, data, left=None, right=None, parent=None):
		self.data = data
		self.left = left
		self.right = right
		self.parent = parent
		self.color = Color.BLACK

	def get_uncle(self):
		if self.is_right_child():
			uncle = self.parent.left
		elif self.is_left_child():
			uncle = self.parent.right
		else:
			uncle = None
		return uncle

	def is_right_child(self):
		if self.parent and self.parent.right == self:
			return True
		else:
			return False

	def is_left_child(self):
		if self.parent and self.parent.left == self:
			return True
		else:
			return False

	def is_root(self):
		return not self.parent

	def get_granpa(self):
		if self.parent and self.parent.parent:
			return self.parent.parent
		else:
			return None

class RedBlackTree(object):
	def __init__(self):
		self.root = None
		self.length = 0

	def insert(self, item):
		self.length += 1
		if not self.root:
			self.root = Node(item)
			self.root.color = Color.BLACK
		else:
			self._insert(self.root, item)

	def _insert(self, root, item):
		if item <= root.data:
			if root.left:
				self._insert(root.left, item)
			else:
				root.left = Node(item)
				root.left.color = Color.RED
				root.left.parent = root
				self.rebalance(root.left)
		else:
			if root.right:
				self._insert(root.right, item)
			else:
				root.right = Node(item)
				root.right.color = Color.RED
				root.right.parent = root
				self.rebalance(root.right)

	def rebalance(self, node):
		if node.is_root():
			node.color = Color.BLACK
		elif node.parent.color != Color.BLACK:
			uncle = node.get_uncle()
			if uncle and uncle.color == Color.RED:
				self._recolor(node)
			else:
				self._rotation(node)
				
	def print_tree(self):
		k = int(math.log(self.length + 1)) + 1
		lines = []
		for lvl in xrange(self.length):
			lines.append([])
		self._print(self.root,lines, 0)
		for line in lines:
			print '-'.join(line)
	
	def _print(self, node, lines, k=None):
		if not node:
			return
		lines[k].append('({0}|{1})'.format(node.data, node.color))
		self._print(node.left, lines, k+1)
		self._print(node.right, lines, k+1)
		

	def _recolor(self, node):
		parent = node.parent
		granpa = node.get_granpa()
		uncle = node.get_uncle()
		if parent:
			parent.color = Color.BLACK
		if uncle:
			uncle.color = Color.BLACK
		if granpa:
			granpa.color = Color.RED
			self.rebalance(self.granpa)                

	def _rotation(self, node):
		parent = node.parent
		granpa = node.get_granpa()
		# Cases
		# 1) Left-Left
		# 2) Left-Right
		# 3) Right-Right
		# 4) Right-Left
		if node.is_left_child() and parent.is_left_child():
			parent.parent = None
			tmp = parent.right
			parent.right = granpa
			if granpa == self.root:
				self.root = parent
			granpa.parent = parent
			granpa.left = tmp
		elif node.is_left_child() and parent.is_right_child():
			grapa.left = node
			node.parent = granpa
			parent.parent = node
			tmp = node.left
			node.left = parent
			parent.right = tmp
			_rotation(self, parent)
		elif node.is_right_child() and parent.is_right_child():
			parent.parent = None
			tmp = parent.left
			parent.left = granpa
			if granpa == self.root:
				self.root = parent
			granpa.parent = parent
			granpa.right = tmp
		else:
			grapa.right = node
			node.parent = granpa
			parent.parent = node
			tmp = node.right
			node.right = parent
			parent.left = tmp
			_rotation(self, parent)
			






tree = RedBlackTree()
tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)
tree.print_tree()





















	

	
