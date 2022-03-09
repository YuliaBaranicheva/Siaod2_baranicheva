import random
import time
A = []
for i in range(25):
    A.append(random.randint(-25, 25))
A.sort()
print(A)

print("Введите значение, которое нужно найти, для функции линейного поиска")
# линейный поиск
a = int(input())
lin_start_time = time.time()

def linear_search(massive, a):
    for i in range(len(massive)):
        if massive[i] == a:
            return i
    return 'В сгенерированном массиве нет элемента с таким значением'
print(linear_search(A, a))
print(f"{(time.time() - lin_start_time)*1000} миллисекунд")

# Вставка элемента
print("Введите элемент, который хотите вставить")
x = int(input())

def insert_elem(massive, x):
    massive.append(x)
    massive.sort()
    return massive

print("Вывод сортированного массива со вставленным элементом: ")
print(insert_elem(A, x))

# Удаление элемента
print("Введите элемент, который хотите удалить")
y = int(input())

def delete_elem(massive, y):
    massive.remove(y)
    massive.sort()
    return massive

print("Вывод сортированного массива с удаленным элементом: ")
print(delete_elem(A, y))


print("Введите значение, которое нужно найти, для функции бинарного поиска")
x = int(input())
bin_start_time = time.time()
def binary_search(massive, x):
    # Нахождение среднего значения
    # Обозначение нижних и верхних границ
    mid = len(massive) // 2
    bot_line = 0
    up_line = len(massive) - 1
    # сравниваем искомое значение с серединой
    while massive[mid] != x and bot_line <= up_line:
        if x > massive[mid]:
            bot_line = mid + 1
        else:
            up_line = mid - 1
        # вычесляем индекс новой середины после сдвига одной из границ
        mid = (bot_line + up_line) // 2
    # проверка условия, если границы пересеклись
    if bot_line > up_line:
        return 'В сгенерированном массиве нет элемента с таким значением'
    else:
        return mid
print(binary_search(A, x))
print(f"{(time.time() - bin_start_time)*1000} миллисекунд")

print("Введите элемент, который хотите вставить")
a = int(input())
print("Вывод сортированного массива со вставленным элементом: ")
print(insert_elem(A, a))
print("Введите элемент, который хотите удалить")
y = int(input())
print("Вывод сортированного массива с удаленным элементом: ")
print(delete_elem(A, y))


# поиск с помощью алогритма бинарного дерева


print("Введите значение, которое нужно найти с помощью фибонначиева поиска")
value = int(input())
fib_start_time = time.time()
def fibonacci_search(massive, value):
    # первые два числа и третье выраженное суммой прошлых
    num_first = 0
    num_second = 1
    num_sumFS = num_first + num_second
    # наименьшее число в последовательности
    while num_sumFS < len(massive):
        num_first = num_second
        num_second = num_sumFS
        num_sumFS = num_first + num_second
    index = -1
    # пока в массиве есть элементы и значением суммы>1 делаем следующее
    while (num_sumFS > 1):
        # i ищем для того, чтобы понять на сколько вниз нам сдвигаться
        i = min(index + num_first, len(massive) - 1)
        if massive[i] < value:
            # перемещаем  наши значения на два шага вниз и индекс становится индексом элемента
            num_sumFS =num_second
            num_second = num_first
            num_first = num_sumFS - num_second
            index = i
        elif massive[i] > value:
            # перемещаем наши значения на один шаг вниз
            num_sumFS = num_first
            num_second = num_second - num_first
            num_first = num_sumFS - num_second
        else:
            return i
    # проверяем значение
    if num_second and index < len(massive) - 1 and massive[index + 1] == value:
        return index + 1
    return 'В сгенерированном массиве нет элемента с таким значением'


print(fibonacci_search(A, value))
print(f"{(time.time() - fib_start_time)*1000} миллисекунд")
print("Введите элемент, который хотите вставить")
a = int(input())
print("Вывод сортированного массива со вставленным элементом: ")
print(insert_elem(A, a))
print("Введите элемент, который хотите удалить")
y = int(input())
print("Вывод сортированного массива с удаленным элементом: ")
print(delete_elem(A, y))


print("Ниже введите значение,для получения результата с помощью интерполяционного поиска")
value = int(input())
int_start_time = time.time()

def interpolation_searsh(massive, value):
    str_index = 0
    lst_index = len(massive) - 1
    while str_index <= lst_index and value >= massive[str_index] and value <= massive[lst_index]:
        # вычисление вероятной позиции искомого элемента
        index = str_index + int(((float(lst_index - str_index) / (massive[lst_index] - massive[str_index])) * (
                value - massive[str_index])))
        # элемент найден
        if massive[index] == value:
            return index
        # пересчитываем индекс для праваого подмассива
        elif massive[index] < value:
            str_index = index + 1
        # пересчитываем индекс для левого подмассива
        else:
            lst_index = index - 1
    return 'В сгенерированном массиве нет элемента с таким значением'


print(interpolation_searsh(A, value))
print(f"{(time.time() - int_start_time)*1000} миллисекунд")
print("Введите элемент, который хотите вставить")
a = int(input())
print("Вывод сортированного массива со вставленным элементом: ")
print(insert_elem(A, a))
print("Введите элемент, который хотите удалить")
y = int(input())
print("Вывод сортированного массива с удаленным элементом: ")
print(delete_elem(A, y))