from collections import deque

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def tree_levels(root):
    if root is None:
       return []

    level = 0
    queue = deque( [(root, level)] )
    levels = {} 

    while queue:
        node = queue.popleft() 

        # append to the array at that level
        if node[1] in levels:
           levels[node[1]].append(node[0].val)
        else:
           # initialize an empty array for paths at that level
           levels[node[1]] = [node[0].val]   
        
        # print queue and paths
        print("queue: ", queue)
        print("paths: ", levels)

        # append left children node
        if node[0].left:
            queue.append((node[0].left, node[1]+1))
        # append right children node 
        if node[0].right:
            queue.append((node[0].right, node[1]+1)) 

    # paths
    paths = []

    # flatten the dictionary
    for level in levels:
        paths.append(levels[level])
    
    # return paths
    return paths
       
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

    paths = tree_levels(a) # ->
    # [
    #   ['a'],
    #   ['b', 'c'],
    #   ['d', 'e', 'f']
    # ]

    print(paths)

    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    g = Node('g')
    h = Node('h')
    i = Node('i')

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    e.right = h
    f.left = i

    #         a
    #      /    \
    #     b      c
    #   /  \      \
    #  d    e      f
    #      / \    /
    #     g  h   i

    paths = tree_levels(a) # ->
    # [
    #   ['a'],
    #   ['b', 'c'],
    #   ['d', 'e', 'f'],
    #   ['g', 'h', 'i']
    # ]

    print(paths)

    q = Node('q')
    r = Node('r')
    s = Node('s')
    t = Node('t')
    u = Node('u')
    v = Node('v')

    q.left = r
    q.right = s
    r.right = t
    t.left = u
    u.right = v

    #      q
    #    /   \
    #   r     s
    #    \
    #     t
    #    /
    #   u
    #  /
    # v

    paths = tree_levels(q) # ->
    # [
    #   ['q'],
    #   ['r', 's'],
    #   ['t'],
    #   ['u'],
    #   ['v']
    # ]
    print(paths)