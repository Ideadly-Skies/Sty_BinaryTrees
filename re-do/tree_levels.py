from collections import deque

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def tree_levels(root):
    if root is None:
       return []

    queue = deque( [(root, 0)] )
    tree_levels = {} 

    while queue:
        node, level = queue.popleft()
        if level not in tree_levels:
           tree_levels[level] = [node.val]
        else:
           tree_levels[level].append(node.val) 

        if node.left:
            queue.append((node.left, level+1))
        if node.right:
            queue.append((node.right, level+1)) 
    
    return [[values for values in tree_levels[level]] for level in tree_levels.keys()] 

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