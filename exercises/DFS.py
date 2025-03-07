# node data structure
class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# stack data structure
def depth_first_values(root, ls=[], isFirst=True):
    if (root is None):
       return ls 
    elif (root.left is None and root.right is None): 
      ls.append(root.val)
      # return_ls
      if isFirst:
        return ls
      return 

    # recursive case 
    ls.append(root.val)
    depth_first_values(root.left, ls)
    depth_first_values(root.right, ls)

    # return final ls
    return ls

if __name__ == "__main__":
    # a = Node('a')
    # b = Node('b')
    # c = Node('c')
    # d = Node('d')
    # e = Node('e')
    # f = Node('f')        
    # a.left = b
    # a.right = c
    # b.left = d
    # b.right = e
    # c.right = f

    #      a
    #    /   \
    #   b     c
    #  / \     \
    # d   e     f

    # ls = depth_first_values(a)
    # #   -> ['a', 'b', 'd', 'e', 'c', 'f']
    # print(ls)

    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    g = Node('g')
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g

    #      a
    #    /   \
    #   b     c
    #  / \     \
    # d   e     f
    #    /
    #   g

    ls = depth_first_values(a)
    #   -> ['a', 'b', 'd', 'e', 'g', 'c', 'f']
    print(ls)