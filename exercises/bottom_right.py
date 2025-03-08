from collections import deque

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def bottom_right_value(root):
    level = 0
    queue = deque( [ (root, level) ] )
    values = []

    while queue:
        node = queue.popleft()
        values.append( (node[0].val, node[1]) )

        print(values)

        # keep maximum level
        level = max(level, node[1]) 
         
        if node[0].left:
            queue.append( (node[0].left, node[1]+1) )
        
        if node[0].right:
            queue.append( (node[0].right, node[1]+1) )

    if len(values) > 1: 
        # pop last two values
        right = values.pop() 
        left = values.pop()
    else:
       # return the sole element 
       return values.pop()[0]

    # both of them are on the same level
    if right[1] == level and left[1] == level:
       return right[0]
    # both of them are not on the same level
    elif right[1] > left[1]:
       return right[0]
    elif right[1] < left[1]:
       return left[0]

if __name__ == "__main__":
    a = Node(3)
    b = Node(11)
    c = Node(10)
    d = Node(4)
    e = Node(-2)
    f = Node(1)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    #       3
    #    /    \
    #   11     10
    #  / \      \
    # 4   -2     1

    value = bottom_right_value(a) # -> 1
    print(value)

    a = Node(-1)
    b = Node(-6)
    c = Node(-5)
    d = Node(-3)
    e = Node(-4)
    f = Node(-13)
    g = Node(-2)
    h = Node(6)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    e.right = h

    #        -1
    #      /   \
    #    -6    -5
    #   /  \     \
    # -3   -4   -13
    #     / \       
    #    -2  6

    value = bottom_right_value(a) # -> 6
    print(value)

    a = Node(-1)
    b = Node(-6)
    c = Node(-5)
    d = Node(-3)
    e = Node(-4)
    f = Node(-13)
    g = Node(-2)
    h = Node(6)
    i = Node(7)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    e.right = h
    f.left = i

    #        -1
    #      /   \
    #    -6    -5
    #   /  \     \
    # -3   -4   -13
    #     / \    /   
    #    -2  6  7 

    value = bottom_right_value(a) # -> 7
    print(value)

    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')

    a.left = b
    a.right = c
    b.right = d
    d.left = e
    e.right = f

    #      a
    #    /   \ 
    #   b     c
    #    \
    #     d
    #    /
    #   e
    #   \
    #    f
            
    value = bottom_right_value(a) # -> 'f'
    print(value)

    a = Node(42)

    #      42

    node = bottom_right_value(a) # -> 42
    print(node)