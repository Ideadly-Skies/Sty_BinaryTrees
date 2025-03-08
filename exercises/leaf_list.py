class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def leaf_list(root):
    if root is None:
        return []
    if (root.left is None and root.right is None):
        return [root.val]

    # list to store all the leaf values
    ls = []
    left = leaf_list(root.left)
    if left:
        # add left leaf list to ls  
        ls += left

    right = leaf_list(root.right)
    if right:
        # add right leaf list to ls 
        ls += right

    # return the list consisting of the leaf nodes
    return ls

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

    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")
    g = Node("g")
    h = Node("h")

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    f.right = h

    #      a
    #    /   \
    #   b     c
    #  / \     \
    # d   e     f
    #    /       \
    #   g         h

    print(leaf_list(a)) # -> [ 'd', 'g', 'h' ]

    a = Node(5)
    b = Node(11)
    c = Node(54)
    d = Node(20)
    e = Node(15)
    f = Node(1)
    g = Node(3)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    e.left = f
    e.right = g

    #        5
    #     /    \
    #    11    54
    #  /   \
    # 20   15
    #      / \
    #     1  3

    print(leaf_list(a)) # -> [ 20, 1, 3, 54 ]

    x = Node('x')

    #      x

    print(leaf_list(x)) # -> [ 'x' ]

    print(leaf_list(None)) # -> [ ]