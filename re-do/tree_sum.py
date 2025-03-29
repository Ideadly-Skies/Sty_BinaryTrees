class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def tree_sum(root):
    if root is None:
       return 0
    left_sum = tree_sum(root.left)
    right_sum = tree_sum(root.right)
    return root.val + left_sum + right_sum

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

    print(tree_sum(a)) # -> 21