import os
import sys

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def is_root(self):
        return not self.parent

    def is_left_child(self):
        return self.parent.left is self

    def is_right_child(self):
        return self.parent.right is self

    def is_leaf(self):
        return not self.left and not self.right

    def __str__(self):
        return '[' + str(self.data) + ']'

class BST(object):
    def __init__(self):
        self.root = None
        self.length = 0

    def insert(self, data):
        self.length += 1
        if not self.root:
            self.root = Node(data)
        else:
            self.__insert(self.root, data)

    def search(self, data):
        return self.__search(self.root, data)

    def __search(self, root, data):
        if not root:
            return None
        elif root.data == data:
            return root
        elif data <= root.data:
            return self.__search(root.left, data)
        else:
            return self.__search(root.right, data)

    def remove(self, data):
        target = self.__search(self.root, data)
        if not target:
            return target
        else:
            tmp = target.data
            self.__remove(target)
            return tmp

    def __remove(self, target):
        # Simple cases, target is leaf
        if target.is_leaf():
            if target.is_left_child():
                target.parent.left = None
            else:
                target.parent.right = None

        # One child
        if target.left and not target.right:
            if target.is_left_child():
                target.parent.left = target.left
            else:
                target.parent.right = target.left

        if target.right and not target.left:
            if target.is_left_child():
                target.parent.left = target.right
            else:
                target.parent.right = target.right

        # Two childs
        if target.left and target.right:
            # Find min from right subtree
            mini = self.__find_minum(target.right)
            # Replace values
            target.data = mini.data
            # Remove minumun element
            self.__remove(mini)        
            

    def __find_minum(self, root):
        if not root.left:
            return root
        return self.__find_minum(root.left)
            
        
    def __insert(self, root, data):
        if data <= root.data:
            if root.left:
                self.__insert(root.left, data)
            else:
                root.left = Node(data)
                root.left.parent = root
        else:
            if root.right:
                self.__insert(root.right, data)
            else:
                root.right = Node(data)
                root.right.parent = root

    def __str__(self):
        string = []
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            string.append(str(current.data))
        return '-'.join(string)


bst = BST()
bst.insert(1)
bst.insert(3)
bst.insert(4)
bst.insert(5)
print bst.search(4)
print bst
bst.remove(4)
print bst
        












    
