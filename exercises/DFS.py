# node data structure
class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# stack data structure
def depth_first_values(root):
  stack = [ root ]
  values = []

  while len(stack) > 0:
    node = stack.pop()
    values.append(node.val)

    # append the right child
    if (node.right):
        stack.append(node.right)
    
    # append the left child
    if (node.left):
      stack.append(node.left)

  # return values traversed
  return values

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

    ls = depth_first_values(a)
    #   -> ['a', 'b', 'd', 'e', 'c', 'f']
    print(ls)

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