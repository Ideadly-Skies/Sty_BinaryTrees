class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def path_finder(root, target):
    # safe guard against potential edge case 
    if root is None:
        return None

    # return root.val
    if root.val == target:
        return [root.val]

    # recursive case
    left_res = path_finder(root.left, target)
    right_res = path_finder(root.right, target)

    # value is going to occur in either subtrees
    # due to constraint
    if left_res:
        return [root.val, *left_res]
    if right_res:
        return [root.val, *right_res]

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

    print(path_finder(a, 'e')) # -> [ 'a', 'b', 'e' ]


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

    print(path_finder(a, 'p')) # -> None