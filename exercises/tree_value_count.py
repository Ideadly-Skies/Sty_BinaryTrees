class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def tree_value_count(root, target):
    if root is None:
       return 0 
    
    stack = [root]
    target_count = 0    

    while len(stack) > 0:
        node = stack.pop()
        if node.val == target:
            target_count += 1

        # append right child
        if (node.right):
           stack.append(node.right)

        # append left child
        if (node.left):
           stack.append(node.left)

    # return target_count
    return target_count

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

    count = tree_value_count(a,  6) # -> 3
    print(count)