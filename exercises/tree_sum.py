from collections import deque

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def tree_sum(root):
    # edge case: empty list 
    if root is None:
       return 0
    
    # initialize values ls and queue
    total = 0 
    queue = deque([ root ])

    # while the queue is not empty
    while queue:
        # popleft from the queue
        value = queue.popleft()
        total += value.val

        # append left and right children to queue
        if value.left is not None:
           queue.append(value.left)
        if value.right is not None:
           queue.append(value.right)

    # return values traversed by BFS
    return total 

if __name__ == "__main__":
    a = Node(3)
    b = Node(11)
    c = Node(4)
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
    #   11     4
    #  / \      \
    # 4   -2     1

    ls = tree_sum(a) # -> 21
    print(ls)