from collections import deque

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def how_high(node):
    if node is None:
        return -1
    
    level = 0 
    queue = deque([ (node, level) ])

    while queue: 
        # grab current value of node
        node = queue.popleft()

        # keep max level
        level = max(level, node[1])

        # add the children
        if node[0].left:
            queue.append( (node[0].left, node[1] + 1) )

        # add the children
        if node[0].right:
            queue.append( (node[0].right, node[1] + 1) )

    return level

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

    level = how_high(a) # -> 2
    print(level)

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

    level = how_high(a) # -> 3
    print(level)