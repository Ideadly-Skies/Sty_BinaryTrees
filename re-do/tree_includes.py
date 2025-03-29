class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def tree_includes(root, target):
    # target is not on the tree  
    if root is None:
       return False

    # check if value equals target 
    if root.val == target:
       return True

    # recursive case 
    left_res = tree_includes(root.left, target)
    right_res = tree_includes(root.right, target)

    # return res on the left subtree or right subtree
    return left_res or right_res

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

    print(tree_includes(a, "e")) # -> True