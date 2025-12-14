"""
Unit tests for the Binary Tree implementation.

This module contains comprehensive tests for all tree operations.
"""

import unittest
from tree import BinaryTree, TreeNode


class TestTreeNode(unittest.TestCase):
    """Test cases for TreeNode class."""
    
    def test_node_creation(self):
        """Test that a node is created correctly."""
        node = TreeNode(10)
        self.assertEqual(node.value, 10)
        self.assertIsNone(node.left)
        self.assertIsNone(node.right)


class TestBinaryTree(unittest.TestCase):
    """Test cases for BinaryTree class."""
    
    def setUp(self):
        """Set up a fresh tree for each test."""
        self.tree = BinaryTree()
    
    def test_empty_tree(self):
        """Test properties of an empty tree."""
        self.assertIsNone(self.tree.root)
        self.assertEqual(self.tree.size(), 0)
        self.assertEqual(self.tree.height(), -1)
        self.assertEqual(self.tree.inorder_traversal(), [])
    
    def test_single_insert(self):
        """Test inserting a single value."""
        self.tree.insert(50)
        self.assertIsNotNone(self.tree.root)
        self.assertEqual(self.tree.root.value, 50)
        self.assertEqual(self.tree.size(), 1)
        self.assertEqual(self.tree.height(), 0)
    
    def test_multiple_inserts(self):
        """Test inserting multiple values."""
        values = [50, 30, 70, 20, 40, 60, 80]
        for value in values:
            self.tree.insert(value)
        
        self.assertEqual(self.tree.size(), 7)
        self.assertEqual(self.tree.height(), 2)
    
    def test_inorder_traversal(self):
        """Test inorder traversal returns sorted values."""
        values = [50, 30, 70, 20, 40, 60, 80]
        for value in values:
            self.tree.insert(value)
        
        result = self.tree.inorder_traversal()
        expected = [20, 30, 40, 50, 60, 70, 80]
        self.assertEqual(result, expected)
    
    def test_preorder_traversal(self):
        """Test preorder traversal."""
        values = [50, 30, 70, 20, 40, 60, 80]
        for value in values:
            self.tree.insert(value)
        
        result = self.tree.preorder_traversal()
        expected = [50, 30, 20, 40, 70, 60, 80]
        self.assertEqual(result, expected)
    
    def test_postorder_traversal(self):
        """Test postorder traversal."""
        values = [50, 30, 70, 20, 40, 60, 80]
        for value in values:
            self.tree.insert(value)
        
        result = self.tree.postorder_traversal()
        expected = [20, 40, 30, 60, 80, 70, 50]
        self.assertEqual(result, expected)
    
    def test_search_existing_values(self):
        """Test searching for values that exist in the tree."""
        values = [50, 30, 70, 20, 40, 60, 80]
        for value in values:
            self.tree.insert(value)
        
        for value in values:
            self.assertTrue(self.tree.search(value))
    
    def test_search_non_existing_values(self):
        """Test searching for values that don't exist."""
        values = [50, 30, 70, 20, 40, 60, 80]
        for value in values:
            self.tree.insert(value)
        
        non_existing = [10, 25, 35, 90, 100]
        for value in non_existing:
            self.assertFalse(self.tree.search(value))
    
    def test_search_empty_tree(self):
        """Test searching in an empty tree."""
        self.assertFalse(self.tree.search(10))
    
    def test_height_single_node(self):
        """Test height of a tree with single node."""
        self.tree.insert(50)
        self.assertEqual(self.tree.height(), 0)
    
    def test_height_balanced_tree(self):
        """Test height of a balanced tree."""
        values = [50, 30, 70, 20, 40, 60, 80]
        for value in values:
            self.tree.insert(value)
        self.assertEqual(self.tree.height(), 2)
    
    def test_height_skewed_tree(self):
        """Test height of a skewed (unbalanced) tree."""
        values = [1, 2, 3, 4, 5]
        for value in values:
            self.tree.insert(value)
        self.assertEqual(self.tree.height(), 4)
    
    def test_size_calculation(self):
        """Test size calculation for various trees."""
        # Empty tree
        self.assertEqual(self.tree.size(), 0)
        
        # After insertions
        for i, value in enumerate([50, 30, 70, 20, 40], 1):
            self.tree.insert(value)
            self.assertEqual(self.tree.size(), i)
    
    def test_duplicate_values(self):
        """Test inserting duplicate values (should go to right subtree)."""
        self.tree.insert(50)
        self.tree.insert(50)
        self.tree.insert(50)
        
        self.assertEqual(self.tree.size(), 3)
        # All duplicates should be in right subtree
        self.assertEqual(self.tree.inorder_traversal(), [50, 50, 50])


class TestTreeTraversalOrders(unittest.TestCase):
    """Test cases specifically for traversal orders."""
    
    def test_small_tree_traversals(self):
        """Test all traversals on a small tree."""
        tree = BinaryTree()
        for value in [5, 3, 7]:
            tree.insert(value)
        
        self.assertEqual(tree.inorder_traversal(), [3, 5, 7])
        self.assertEqual(tree.preorder_traversal(), [5, 3, 7])
        self.assertEqual(tree.postorder_traversal(), [3, 7, 5])
    
    def test_complex_tree_traversals(self):
        """Test all traversals on a more complex tree."""
        tree = BinaryTree()
        values = [5, 3, 7, 2, 4, 6, 8, 1]
        for value in values:
            tree.insert(value)
        
        self.assertEqual(tree.inorder_traversal(), [1, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(tree.preorder_traversal(), [5, 3, 2, 1, 4, 7, 6, 8])
        self.assertEqual(tree.postorder_traversal(), [1, 2, 4, 3, 6, 8, 7, 5])


if __name__ == '__main__':
    unittest.main()
