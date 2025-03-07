from collections import deque

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def tree_includes(root, target):
    # edge-case: root is None
    if root is None:
        return False
    
    # create a deque w/ root
    queue = deque([ root ])

    while queue:
        # pop the node from the deque
        node = queue.popleft()
        
        # check if dequeued node equals target 
        if node.val == target:
            return True

        # check if children equals target
        if node.left is not None:
           queue.append(node.left)            
        if node.right is not None:
           queue.append(node.right)

    # tree does not contain target value
    return False

if __name__ == "__main__":
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")

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
    print(tree_includes(a, "a")) # -> True
