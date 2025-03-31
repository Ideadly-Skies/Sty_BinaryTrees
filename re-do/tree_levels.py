from collections import deque

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def tree_levels(root):
    # create a queue 
    queue = deque([(root, 0)])
    levels = {} 
     
    # BFS traversal 
    while queue:
        curr, level = queue.popleft()

        if level not in levels:
            levels[level] = [curr.val]
        else:
            levels[level].append(curr.val) 
         
        if curr.left:
            queue.append((curr.left, level+1))
        if curr.right:
            queue.append((curr.right, level+1))
    
    return list(levels.values())
        
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

    print(tree_levels(a)) # ->
    # [
    #   ['a'],
    #   ['b', 'c'],
    #   ['d', 'e', 'f']
    # ]