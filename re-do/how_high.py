class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def how_high(node, level=0):
    # protect against edge case 
    if node is None:
        return -1  

    # base case
    if node.left is None and node.right is None:
        return level
    
    # recursive case
    left_level = how_high(node.left, level+1)
    right_level = how_high(node.right, level+1) 

    # return max_level 
    return max(left_level, right_level) 
     
if __name__ == "__main__":
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    #      a
    #    /   \
    #   b     c
    #  / \     \
    # d   e     f

    print(how_high(a)) # -> 2
    
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    g = Node('g')

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g

    #      a
    #    /   \
    #   b     c
    #  / \     \
    # d   e     f
    #    /
    #   g

    print(how_high(a)) # -> 3
    
    a = Node('a')
    c = Node('c')

    a.right = c

    #      a
    #       \
    #        c

    print(how_high(a)) # -> 1
    
    a = Node('a')

    #      a

    print(how_high(a)) # -> 0