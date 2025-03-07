from collections import deque

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def tree_min_value(root):
    # set starting min value to root.val 
    min_value = root.val 

    queue = deque([ root ])

    while queue:
        # pop current leftmost node
        node = queue.popleft()
        min_value = min(node.val, min_value)

        # append children into queue
        if node.left is not None:
           queue.append(node.left)
        if node.right is not None:
           queue.append(node.right)

    return min_value

if __name__ == "__main__":
    a = Node(5)
    b = Node(11)
    c = Node(3)
    d = Node(4)
    e = Node(14)
    f = Node(12)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    #       5
    #    /    \
    #   11     3
    #  / \      \
    # 4   14     12

    min_value = tree_min_value(a) # -> 3
    print(min_value)