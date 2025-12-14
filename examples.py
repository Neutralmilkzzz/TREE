"""
Example usage of the Binary Tree implementation.

This script demonstrates various tree operations including:
- Creating a tree
- Inserting values
- Different traversal methods
- Searching for values
- Getting tree properties
"""

from tree import BinaryTree


def main():
    print("=" * 50)
    print("Binary Tree Study - Examples")
    print("=" * 50)
    
    # Create a new binary tree
    bt = BinaryTree()
    
    # Insert values
    print("\n1. Inserting values: 50, 30, 70, 20, 40, 60, 80")
    values = [50, 30, 70, 20, 40, 60, 80]
    for value in values:
        bt.insert(value)
    
    # Tree visualization (conceptual)
    print("\nTree structure:")
    print("       50")
    print("      /  \\")
    print("    30    70")
    print("   /  \\  /  \\")
    print("  20 40 60  80")
    
    # Demonstrate traversals
    print("\n2. Tree Traversals:")
    print(f"   Inorder (Left-Root-Right):   {bt.inorder_traversal()}")
    print(f"   Preorder (Root-Left-Right):  {bt.preorder_traversal()}")
    print(f"   Postorder (Left-Right-Root): {bt.postorder_traversal()}")
    
    # Search for values
    print("\n3. Search operations:")
    search_values = [40, 90, 20, 100]
    for val in search_values:
        found = bt.search(val)
        print(f"   Search for {val}: {'Found' if found else 'Not found'}")
    
    # Tree properties
    print("\n4. Tree properties:")
    print(f"   Tree height: {bt.height()}")
    print(f"   Tree size (number of nodes): {bt.size()}")
    
    # Create another example tree
    print("\n" + "=" * 50)
    print("Creating another tree with values: 5, 3, 7, 2, 4, 6, 8, 1")
    print("=" * 50)
    
    bt2 = BinaryTree()
    for value in [5, 3, 7, 2, 4, 6, 8, 1]:
        bt2.insert(value)
    
    print("\nTree structure:")
    print("       5")
    print("      / \\")
    print("     3   7")
    print("    / \\ / \\")
    print("   2  4 6  8")
    print("  /")
    print(" 1")
    
    print(f"\nInorder traversal: {bt2.inorder_traversal()}")
    print(f"Tree height: {bt2.height()}")
    print(f"Tree size: {bt2.size()}")
    
    print("\n" + "=" * 50)
    print("Examples completed!")
    print("=" * 50)


if __name__ == "__main__":
    main()
