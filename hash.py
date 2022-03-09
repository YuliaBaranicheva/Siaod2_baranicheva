# Создадим класс хэш-таблицы

class hash_table:
    size = int(input("Укажите размерность хэш-таблицы: "))

    def __init__(self):
        self.data = [None] * self.size

    # Получение содержимого баккета
    def __getitem__(self, key):
        h = self.getHash(key)
        try:
            while self.data[h]:
                if self.data[h] and self.data[h].get(key):
                    return self.data[h]
                h = self.getRehash(h)
        except IndexError:
            return
    #Заполнение пустого баккета
    def __setitem__(self, key, value):
        h = self.getHash(key)
        if self.data[h] is None:
            self.data[h] = {key: value}
            return
        next_h = self.getRehash(h)
        try:
            while self.data[next_h] is not None:
                if self.data[next_h].get(key):
                    self.data[next_h].get(key)
                    break
                next_h = self.getRehash(next_h)
        except IndexError:
            raise
        self.data[next_h] = {key: value}

    # Функция хэширования
    def getHash(self, name):
        return len(name) % self.size

    # Функция рехэширования
    def getRehash(self, oldhash):
        return oldhash + 1

# Заполним хэш-таблицу значениями
table = hash_table()
table[input('\n Ключ - ')] = input('\n Значение -  ')
table[input('\n Ключ - ')] = input('\n Значение -  ')

# Вывод одного из значений через ключ
print(table[input('\nВыберите значение по ключу: ')])


