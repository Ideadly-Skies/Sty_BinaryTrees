
# import double ended queue
from collections import deque

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def breadth_first_values(root, ls=[], isFirst=True):
    if root is None:
       return []

    values = []      # to store the BFS traversal
    queue = deque([ root ]) # using queue DS
    
    while queue:
        current = queue.popleft() # O(1)
        values.append(current.val)

        if current.left:
            queue.append(current.left)

        if current.right:
           queue.append(current.right)

    return values

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

    # ls = breadth_first_values(a) 
    #    -> ['a', 'b', 'c', 'd', 'e', 'f']
    # print(ls)

    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    g = Node('g')
    h = Node('h')

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    f.right = h

    #      a
    #    /   \
    #   b     c
    #  / \     \
    # d   e     f
    #    /       \
    #   g         h

    ls = breadth_first_values(a) 
    #   -> ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    print(ls)