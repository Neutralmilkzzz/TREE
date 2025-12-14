"""
Binary Tree Data Structure Implementation

This module provides a basic implementation of a binary tree data structure
with common operations like insertion, traversal, and search.
"""


class TreeNode:
    """Represents a node in a binary tree."""
    
    def __init__(self, value):
        """
        Initialize a tree node.
        
        Args:
            value: The value to store in the node
        """
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    """Binary Tree implementation with common operations."""
    
    def __init__(self):
        """Initialize an empty binary tree."""
        self.root = None
    
    def insert(self, value):
        """
        Insert a value into the binary tree.
        
        Args:
            value: The value to insert
        """
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        """
        Recursively insert a value into the tree.
        
        Args:
            node: Current node
            value: Value to insert
        """
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)
    
    def search(self, value):
        """
        Search for a value in the tree.
        
        Args:
            value: The value to search for
            
        Returns:
            True if value exists, False otherwise
        """
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, node, value):
        """
        Recursively search for a value.
        
        Args:
            node: Current node
            value: Value to search for
            
        Returns:
            True if found, False otherwise
        """
        if node is None:
            return False
        if node.value == value:
            return True
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)
    
    def inorder_traversal(self):
        """
        Perform inorder traversal (Left -> Root -> Right).
        
        Returns:
            List of values in inorder sequence
        """
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        """Helper method for inorder traversal."""
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)
    
    def preorder_traversal(self):
        """
        Perform preorder traversal (Root -> Left -> Right).
        
        Returns:
            List of values in preorder sequence
        """
        result = []
        self._preorder_recursive(self.root, result)
        return result
    
    def _preorder_recursive(self, node, result):
        """Helper method for preorder traversal."""
        if node:
            result.append(node.value)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)
    
    def postorder_traversal(self):
        """
        Perform postorder traversal (Left -> Right -> Root).
        
        Returns:
            List of values in postorder sequence
        """
        result = []
        self._postorder_recursive(self.root, result)
        return result
    
    def _postorder_recursive(self, node, result):
        """Helper method for postorder traversal."""
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.value)
    
    def height(self):
        """
        Calculate the height of the tree.
        
        Returns:
            The height of the tree (number of edges in longest path from root to leaf)
        """
        return self._height_recursive(self.root)
    
    def _height_recursive(self, node):
        """Helper method to calculate height recursively."""
        if node is None:
            return -1
        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)
        return max(left_height, right_height) + 1
    
    def size(self):
        """
        Get the number of nodes in the tree.
        
        Returns:
            Number of nodes in the tree
        """
        return self._size_recursive(self.root)
    
    def _size_recursive(self, node):
        """Helper method to count nodes recursively."""
        if node is None:
            return 0
        return 1 + self._size_recursive(node.left) + self._size_recursive(node.right)
