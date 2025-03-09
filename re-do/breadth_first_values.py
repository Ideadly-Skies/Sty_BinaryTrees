from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def breadth_first_values(root):
    if root is None:
        return []
    
    values = []
    queues = deque([ root ])

    while queues:
        node = queues.popleft()
        values.append(node.val)

        if node.left:
            queues.append(node.left)
        if node.right:
            queues.append(node.right)

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
