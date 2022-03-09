
class ChainMethod:
    def __init__(self):
        self.data = [None]*64
    def _hash(self,key):
        return hash(key)%(2**4)
    def addItem(self, index, key):
        if self.data[index] is None:
            self.data[index] = [key]
            print("элемент был добавлен")
            return 1
        else:
            for i, item in enumerate(self.data[index]):
                if item == key:
                    self.data[index][i] = key
                    print("элемент не был добавлен")
                    return 0
            self.data[index].append(key)
            print("элемент был добавлен")
            return 1
    def searchChain(self,index,item):
        if self.data[index] is not None:
            if self.data[index] == [item]:
                print("Элемент был найден")
                return 1
            else:
                for i, item_ in enumerate(self.data[index]):
                    if self.data[index][i] == item:
                        print("Элемент был найден")
                        return 1
        else:
            print("Элемент не найден")
            return 0
    def deleteItem_Chain(self,index,item):
        if self.data[index] is not None:
            if self.data[index] == [item]:
                self.data[index] = None
                print("Элемент был удален")
                return 1
            else:
                for i, item_ in enumerate(self.data[index]):
                    if self.data[index][i] == item:
                        self.data[index].pop(i)
                        print("Элемент был удален")
                        return 1
        else:
            return 0
tableChain = ChainMethod()
tableChain.addItem(tableChain._hash("Привет"),"Привет")
tableChain.addItem(tableChain._hash("Салют"),"Салют")
tableChain.addItem(tableChain._hash("День"),"День")
tableChain.searchChain(tableChain._hash("День"),"День")
tableChain.deleteItem_Chain(tableChain._hash("Салют"),"Салют")
