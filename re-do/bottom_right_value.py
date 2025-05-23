from collections import deque

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def bottom_right_value(root):
    # create a queue 
    queue = deque([(root, 0)])
    levels = [(root.val, 0)] 
     
    # BFS traversal 
    while queue:
        curr, level = queue.popleft()

        if curr.left:
            queue.append((curr.left, level+1))
            levels.append((curr.left.val, level+1))
        if curr.right:
            queue.append((curr.right, level+1))
            levels.append((curr.right.val, level+1)) 

    return levels[-1][0]
    
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

    print(bottom_right_value(a)) # -> 1
    
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

    print(bottom_right_value(a)) # -> 6
    
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

    print(bottom_right_value(a)) # -> 7
    
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
            
    print(bottom_right_value(a)) # -> 'f'
    
    a = Node(42)

    #      42

    print(bottom_right_value(a)) # -> 42