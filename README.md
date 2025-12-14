# TREE - Binary Tree Study Project

A comprehensive implementation of binary tree data structures in Python for educational purposes.

## Overview

This project provides a well-documented implementation of a binary tree with common operations including insertion, search, and various traversal methods (inorder, preorder, postorder).

## Features

- **Binary Tree Implementation**: Full-featured binary search tree
- **Tree Operations**:
  - Insert values
  - Search for values
  - Calculate tree height
  - Count nodes (size)
- **Traversal Methods**:
  - Inorder traversal (Left → Root → Right)
  - Preorder traversal (Root → Left → Right)
  - Postorder traversal (Left → Right → Root)
- **Comprehensive Tests**: Full test suite using Python's unittest framework
- **Examples**: Practical examples demonstrating tree usage

## Files

- `tree.py` - Main binary tree implementation
- `examples.py` - Example usage and demonstrations
- `test_tree.py` - Comprehensive unit tests

## Usage

### Basic Example

```python
from tree import BinaryTree

# Create a new binary tree
bt = BinaryTree()

# Insert values
bt.insert(50)
bt.insert(30)
bt.insert(70)
bt.insert(20)
bt.insert(40)

# Search for a value
found = bt.search(30)  # Returns True
not_found = bt.search(100)  # Returns False

# Get inorder traversal (sorted order for BST)
values = bt.inorder_traversal()  # [20, 30, 40, 50, 70]

# Get tree properties
height = bt.height()  # Height of the tree
size = bt.size()  # Number of nodes
```

### Running Examples

```bash
python examples.py
```

This will demonstrate:
- Creating trees
- Inserting values
- All three traversal methods
- Searching for values
- Tree properties (height and size)

### Running Tests

```bash
python test_tree.py
```

Or with verbose output:

```bash
python test_tree.py -v
```

## Tree Structure

The binary tree maintains the binary search tree property:
- Values less than a node go to the left subtree
- Values greater than or equal to a node go to the right subtree

Example tree after inserting [50, 30, 70, 20, 40, 60, 80]:

```
       50
      /  \
    30    70
   /  \  /  \
  20 40 60  80
```

## Traversal Methods

### Inorder Traversal (Left → Root → Right)
Visits nodes in sorted order for a BST.
Result: `[20, 30, 40, 50, 60, 70, 80]`

### Preorder Traversal (Root → Left → Right)
Visits root before children, useful for copying a tree.
Result: `[50, 30, 20, 40, 70, 60, 80]`

### Postorder Traversal (Left → Right → Root)
Visits children before root, useful for deleting a tree.
Result: `[20, 40, 30, 60, 80, 70, 50]`

## Learning Resources

This implementation covers fundamental tree concepts:

1. **Binary Tree Structure**: Each node has at most two children
2. **Binary Search Tree Property**: Left < Root ≤ Right
3. **Recursive Algorithms**: All operations use recursion
4. **Tree Traversals**: Understanding different visiting orders
5. **Tree Properties**: Height, size calculations

## Requirements

- Python 3.6 or higher
- No external dependencies required

## License

This is an educational project for studying tree data structures.