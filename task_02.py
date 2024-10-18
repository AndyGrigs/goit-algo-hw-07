class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def min_node(root):
    # Перевіряємо, чи дерево порожнє
    if root is None:
        return None

    # Рухаємося до крайнього лівого вузла
    current_node = root
    while current_node.left is not None:
        current_node = current_node.left
    
    # Найменший елемент у дереві
    return current_node.val

# Створюємо просте двійкове дерево пошуку
root = TreeNode(20)
root.left = TreeNode(10)
root.right = TreeNode(30)
root.left.left = TreeNode(5)

min = min_node(root)
print(f"Найменший елемент у дереві: {min}")