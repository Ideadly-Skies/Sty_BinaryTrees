class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def max_path_sum(root):
    if root is None:
       return float("-inf")

    if root.left is None and root.right is None:
        return root.val

    left = max_path_sum(root.left)
    right = max_path_sum(root.right)

    return root.val + max(left, right)

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

    print(max_path_sum(a)) # -> 18