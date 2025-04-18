class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def tree_value_count(root, target):
    # guard against edge case 
    if root is None:
        return 0

    # recursive case
    left_res = tree_value_count(root.left, target)
    right_res = tree_value_count(root.right, target)
    match = 1 if root.val == target else 0

    return match + left_res + right_res

if __name__ == "__main__":
    a = Node(12)
    b = Node(6)
    c = Node(6)
    d = Node(4)
    e = Node(6)
    f = Node(12)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    #      12
    #    /   \
    #   6     6
    #  / \     \
    # 4   6     12

    print(tree_value_count(a,  6)) # -> 3

    a = Node(12)
    b = Node(6)
    c = Node(6)
    d = Node(4)
    e = Node(6)
    f = Node(12)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    #      12
    #    /   \
    #   6     6
    #  / \     \
    # 4  6     12

    print(tree_value_count(a,  12)) # -> 2