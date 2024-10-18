class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def max_node(root):
     # Перевіряємо, чи дерево порожнє
    if root is None:
        return None
    # Рухаємося до крайнього правого вузла
    cur_node = root
    while cur_node.right is not None:
        cur_node = cur_node.right
    # Найбільший елемент у дереві
    return cur_node.val

root = TreeNode(100)
root.left = TreeNode(30)
root.left = TreeNode(34)
root.right = TreeNode(64)
root.right.right = TreeNode(84)

max = max_node(root)
print(f"Найбільший елемент у дереві: {max}")
