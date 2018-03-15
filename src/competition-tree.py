""" 
Given a competition tree - find the second largest 
"""

class Node: 
    def __init__(self, v, l=None, r=None):
        self.val = v
        self.lt = l 
        self.rt = r
    
    def has_children(self):
        return self.lt is not None

    def __str__(self):
        return "[{0} - L{1}, R{2}]".format(self.val, self.lt, self.rt)

class CompetitionTree: 
    """
    Binary tree with competition nodes 
    """

    def __init__(self, n=None):
        self.root = n


    def create_dummy(self):
        n_leaves = 10 
        nodes = [Node(i) for i in range(n_leaves)]
        while len(nodes) > 1:
            i = 0
            new_nodes = []
            while i < len(nodes): 
                l = nodes[i] 
                r = nodes[i+1]
                root = Node(r.val)
                root.lt = l 
                root.rt = r
                new_nodes.append(root)
                print(root)
                i = i+2
            nodes = new_nodes
        self.root = nodes[0]



    def find_second_max(self):
        import sys
        if self.root is None: 
            return None
        n = self.root
        max_val = self.root.val
        second_max = -1  
        while n.has_children():
            if n.lt.val == max_val: 
                if n.rt.val > second_max:
                    second_max = n.rt.val
                n = n.lt 
            else:
                assert n.rt.val == max_val
                if n.lt.val > second_max:
                    second_max = n.lt.val
                n = n.rt
        
        return second_max

    """
    Assume competition numbers are postive ints 
    """
    def find_second_max2(self):
        if self.root is None:
            return -1

        n = self.root
        max_val = n.val
        second_max = -1 

        while n.has_children():
            if n.lt.val == max_val and n.rt.val > second_max : 
                second_max = n.rt.val
                n = n.lt
            elif n.lt.val > second_max:
                assert n.rt.val == max_val
                second_max = n.lt.val
                n = n.rt
        return second_max

    def find_kth_max(self):
        

def main():
    #c.create_dummy()
    n1 = Node(10, Node(10), Node(9, Node(9), Node(8)))
    n2 = Node(6, Node(6), Node(5, Node(5), Node(4)))
    n = Node(10, n1, n2 )
    c = CompetitionTree(n)
    print (c.find_second_max2())


if __name__ == "__main__":
    main()