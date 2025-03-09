from collections import deque

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def level_averages(root):
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
    
    res = [[values for values in tree_levels[level]] for level in tree_levels.keys()] 
    return [sum(values)/len(values) for values in res]

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

    print(level_averages(a)) # -> [ 3, 7.5, 1 ] 
    