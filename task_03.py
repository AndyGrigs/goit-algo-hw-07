class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def sum_of_nodes(root):
    # Якщо дерево порожнє, сума дорівнює 0
    if root is None:
        return 0
    # Рекурсивно обчислюємо суму лівого і правого піддерев і додаємо поточне значення вузла
    return root.val + sum_of_nodes(root.left) + sum_of_nodes(root.right)    


root = TreeNode(50)
root.left = TreeNode(23)
root.right = TreeNode(34)
root.left.left = TreeNode(20)
root.right.right = TreeNode(14)

sum = sum_of_nodes(root)
print(f"Сума всіх елементів у дереві: {sum}")