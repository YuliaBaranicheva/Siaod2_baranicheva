import random

A = []
for i in range(25):
    A.append(random.randint(-25,25))

print(A)
# Создаем узел
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Сортируем дерево
def inorder(root):
    if root is not None:

        # Обходим левое поддерево
        inorder(root.left)

        # Обходим корень
        print(str(root.key) + " ", end=' ')

        # Обходим правое поддерево
        inorder(root.right)

#поиск элемента
def searchItem(self, key):
    if self.key:
        if self.key == key:
            print("Элемент найден")
            return
        if key < self.key:
            if self.left is None:
                print("Элемент не найден")
                return self.left.searchItem(key)
        else:
            if self.right is None:
                print("Элемент не найден")
                return self.right.searchItem(key)
    else:
        print("Дерево пустое")

# Вставка элемента
def insert(node, key):
    # Возвращаем новый узел, если дерево пустое
    if node is None:
        return Node(key)

    # Идем в нужное место и вставляет узел
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node

# Поиск inorder-преемника
def minValueNode(node):
    current = node
    # Найдем крайний левый лист — он и будет inorder-преемником
    while(current.left is not None):
        current = current.left
    return current

# Удаление узла
def deleteNode(root, key):
    # Возвращаем, если дерево пустое
    if root is None:
        return root

    # Найдем узел, который нужно удалить
    if key < root.key:
        root.left = deleteNode(root.left, key)
    elif(key > root.key):
        root.right = deleteNode(root.right, key)
    else:
        # Если у узла только один дочерний узел или вообще их нет
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # Если у узла два дочерних узла,
        # помещаем центрированного преемника
        # на место узла, который нужно удалить
        temp = minValueNode(root.right)

        root.key = temp.key

        # Удаляем inorder-преемниа
        root.right = deleteNode(root.right, temp.key)

    return root


root = None
for i in range(len(A)):
    root = insert(root, A[i])

print("\nСортируем: ", end=' ')
inorder(root)

print("\nВведите элемент, который хотите удалить: ")
del_value = int(input())
root = deleteNode(root, del_value)
print("Вывод сортированный массив с удаленным элементом: ", end=' ')
inorder(root)

print("\nВведите элемент, который хотите вставить: ")
ins_value = int(input())
root = insert(root,ins_value)
print("Вывод сортированный массив со вставленным элементом: ", end=' ')
inorder(root)