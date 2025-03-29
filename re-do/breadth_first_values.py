from collections import deque

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def breadth_first_values(root):
    # edge case
    if root is None:
       return [] 
    
    # init queue with root 
    queue = deque([root])
    
    # values to store all traversed values
    values = []

    while queue:
        # get current node from queue 
        curr = queue.popleft()
        values.append(curr.val)
        
        # enqueue children to queue 
        if curr.left:
           queue.append(curr.left)
        if curr.right:
           queue.append(curr.right)
        
    # return the list of values traversed
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

    print(breadth_first_values(a)) 
    #    -> ['a', 'b', 'c', 'd', 'e', 'f']

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

    print(breadth_first_values(a)) 
    #   -> ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    a = Node('a')

    #      a

    print(breadth_first_values(a)) 
    #    -> ['a']

    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    x = Node('x')

    a.right = b
    b.left = c
    c.left = x
    c.right = d
    d.right = e

    #      a
    #       \
    #        b
    #       /
    #      c
    #    /  \
    #   x    d
    #         \
    #          e

    print(breadth_first_values(a)) 
    #    -> ['a', 'b', 'c', 'x', 'd', 'e']