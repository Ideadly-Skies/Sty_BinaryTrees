class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def leaf_list(root):
    if root is None:
        return []
    
    if root.left is None and root.right is None:
        return [root.val]
    
    left_res = leaf_list(root.left)
    right_res = leaf_list(root.right)
    
    return [*left_res, *right_res]

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

    print(leaf_list(a)) # -> [ 'd', 'e', 'f' ]