import os
import sys

# Implementation of AVL Tree

class TreeNode(object):
    def __init__(self, data, left=None, right=None, parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.balance = 0
        self.parent = parent

    def is_left_child(self):
        if not parent:
            return False
        return parent.left == self

    def is_right_child(self):
        if not parent:
            return False
        return parent.right == self

    def __cmp__(self, other):
        if not other or not isinstance(other, TreeNode):
            return 1
        if self.data == other.data:
            return 0
        elif self.data > other.data:
            return 1
        else:
            return -1

    def is_root(self):
        return not self.parent

    def __str__(self):
            return '{0}<-{1}->{2}'.format(str(self.left),
                                          str(self.data),
                                          str(self.right))


class AVLTree(object):
    def __init__(self):
        self.root = None


    def insert(self, item):
        if not self.root:
            self.root = TreeNode(item)
        else:
            self._insert(self.root, item)

    def _insert(self, root, item):
        if item < root.data:
            if root.left:
                self._insert(root.left, item)
            else:
                root.left = TreeNode(item, parent=root)
                self._updata_balance(root.left)
        else:
            if root.right:
                self._insert(root.right, item)
            else:
                root.right = TreeNode(item, parent=root) 
                self._updata_balance(root.right)


    # We have just inserted a new node, rebalance count
    def _update_balance(self, root):
        if root.balance > 1 or root.balance < -1:
            self.rebalance(root)
            return
        if root.parent:
            if root.is_left_child():
                root.parent.balance +=1
            elif root.is_right_child():
                root.parent.balance -= 1

            if root.parent.balance != 0:
                self._update_balance(root.parent)
        

    def rebalance(self, root):
        if root.balance < 0:
            if node.right.balance > 0:
                self._rotate_right(root.right)
                self._rotate_left(root)
            else:
                self._rotate_left(root)
        elif root.balance > 0:
            if node.left.balance < 0:
                self._rotate_left(root.left)
                self._rotate_right(root)
            else:
                self._rotate_right(root)

    def __rotate_left(self, root):
        new_root = root.right
        root.right = new_root.left

        if new_root.left:
            new_root.left.parent = root

        if root.is_root():
            self.root = new_root
        else:
            if root.is_left_child():
                root.parent.left = new_root
            else:
                root.parent.right = new_root

        new_root.left = root
        root.parent = new_root
        root.balance = root.balance + 1 - min(new_root.balance, 0)
        new_root.balance = root.balance + 1 + max(new_root.balance, 0)


    def __rotate_right(self, root):
        new_root = root.left
        root.right = new_root.right

        if new_root.right:
            new_root.right.parent = root

        if root.is_root():
            self.root = new_root
        else:
            if root.is_right_child():
                root.parent.right = new_root
            else:
                root.parent.left = new_root

        new_root.right = root
        root.parent = new_root
        root.balance = root.balance + 1 - min(new_root.balance, 0)
        new_root.balance = root.balance + 1 + max(new_root.balance, 0)

        






















        
