from collections import deque

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def level_averages(root):
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
        paths.append(sum(levels[level])/len(levels[level]))
    
    # return paths
    return paths

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

    averages = level_averages(a) # -> [ 3, 7.5, 1 ] 
    print(averages)