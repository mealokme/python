f"""
Problem: 
Given a binary tree of integers, print the longest sequence of consecutive integers that occur along any path from root to a leaf. 
The sequence can start and end anywhere along the path. 
"""


class Node: 
    """
    A node of a binary tree 
    
    Stores integer value and references to left and right children
    """
    
    def __init__(self, val, left_child=None, right_child=None):
        """
        Constructor takes an int and optional children nodes 
        
        """
        self.val = val
        self.lt = left_child
        self.rt = right_child
    
    @property
    def left(self):
        """
        Returns:
            the left child of node
        """
        return self.lt 

    @left.setter
    def left(self, node):
        """
        sets the left child of the node
        Args:
            node : a Node instance to set as left child
        """
        self.lt = node
    
    @property
    def right(self):
        """
        Returns:
            the right child of node
        """
        return self.rt

    @right.setter
    def right(self, node):
        """
        sets the right child of the node
        Args:
            node : a Node instance to set as right child
        """
        self.rt = node
    


import random  # used for creating Node instances with random values  

class BinaryTree: 
    """
    Binary tree class. It does not enforce any ordering on nodes
    """

    def __init__(self):
        """
        Constructor to create an empty BinaryTree
        """
        self._root = None
    
    @property
    def root(self):
        """
        Returns:
            The root of the binary tree 
        """
        return self._root
    
    def insert_random(self, node): 
        """
        Inserts 'node' as a leaf by randomly traversing left or right subtree
        Args:
            node: a Node to insert into the tree 
        """
        if self._root is None:
            self._root = node 
            return 
        n = self._root 

        while (n is not None): 
            # make a random choice whether to insert left or right 
            insert_left = random.choice([True, False])
            if insert_left: 
                if n.left is None:
                    n.left = node
                    break
                n = n.left
            else:
                if n.right is None:
                    n.right = node 
                    break
                n = n.right

    def print(self):
        """
        Utility method to print the binary tree
        """
        if self.root is None: 
            print("Empty Tree")
        else:
            level_nodes = [(self.root, "ROOT::{}".format(self.root.val))]
            while level_nodes:
                new_level = list()
                level_str = list()
                for n_tup in level_nodes:
                    level_str.append(n_tup[1])
                    n = n_tup[0]
                    if n is not None and (n.left is not None or n.right is not None):
                        new_level.append((None, "[P::{}".format(n.val)))
                        if n.left: 
                            new_level.append((n.left, "[L:{}".format(n.left.val)))
                        else:
                            new_level.append((None,  "[L:None"))
                        if  n.right:
                            new_level.append((n.right,  "R:{}]]".format(n.right.val)))
                        else:
                            new_level.append((None,  "R:None]]"))

                print(" ".join(level_str))
                level_nodes = new_level


    def longest_consecutive_path(self):
        """
        Finds the longest consecutive sequence of integers in a path from root to leaf
        Returns:
            String representation of the longest consecutive path sequence
        """
        if self.root is None: 
            return "Tree Empty"
        
        path_nodes = self.longest_consecutive_path_dfs(self.root, [None])

        return ",".join([str(x.val) for x in path_nodes])

    def longest_consecutive_path_dfs(self, node, prefix): 
        """
        Depth first routine to find the longest consecutive path passing through node 
        Args:
            node: a tree node through which longest consecutive path needs to be found.
            prefix: List of prefix tree nodes to include in the consecutive path through node
        Returns:
            longest consecutive path through or under node. 
        """

        if node is None:
            return None
        node_path = [node]
        parent = prefix[-1]
        if parent is not None and node.val == parent.val + 1:
            node_path = prefix + node_path

        left_path = self.longest_consecutive_path_dfs(node.left, node_path)
        right_path = self.longest_consecutive_path_dfs(node.right, node_path)

        return max([node_path, left_path, right_path], key=lambda x: 0 if x is None else len(x))
        

    # static range for node values used when creating a dummy tree
    DUMMY_RANGE = 100

    @staticmethod
    def build_test_tree():
        """
        Create some dummy trees for testing
        """
        r = Node(8)
        r = Node(8, Node(2, Node(5), Node(3, Node(4))), Node(6, Node(7), Node(10)))
        r = Node(1, Node(2, Node(5), Node(3, Node(41))), Node(6, Node(7), Node(10)))
        r = Node(1, Node(21, Node(5), Node(31, Node(41))), Node(6, Node(7), Node(10)))
        r = Node(11, Node(21, Node(5), Node(31, Node(41))), Node(12, Node(13), Node(10)))
        
        tree = BinaryTree()
        tree.insert_random(r)
        return tree

    @staticmethod
    def build_random_dummy_tree(n):
        """
        Create a dummy tree with 'n' nodes inserted incrementally at random leaf locations
        Args:
            n: the number of nodes to be inserted into the tree
        """
        tree = BinaryTree()
        for i in range(n):
            tree.insert_random(Node(random.randint(0,BinaryTree.DUMMY_RANGE)))
        return tree 


def main():
    bt = BinaryTree.build_test_tree()
    bt.print()
    path = bt.longest_consecutive_path()
    print("Longest path with consecutive numbers " + path)

if __name__ == "__main__":
    main()