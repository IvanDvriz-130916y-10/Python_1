class Node:
    """
    Вспомогательный класс для узлов списка
    """

    def __init__(self, data):
        self.data = data  # храним информацию
        self.nref = None  # ссылка на следующий узел
        self.pref = None  # ссылка на предыдущий узел


class Queue:
    """
    Основной класс
        """

    def __init__(self):
        self.start = None  # ссылка на начало очереди
        self.end = None  # ссылка на конец очереди

    def pop(self):
        """
        Возвращаем элемент из начала списка с удалением его из списка
        """
        if self.start is None:
            raise IndexError("pop from empty queue")

        val = self.start.data  # сохраняем значение первого элемента
        self.start = self.start.nref  # перемещаем указатель на следующий элемент

        if self.start is not None:
            self.start.pref = None  # обновляем ссылку на предыдущий узел
        else:
            self.end = None  # если очередь стала пустой, обновляем конец

        return val  # возвращаем значение

    def push(self, val):
        """
        Добавление элемента val в конец списка
        """
        new_node = Node(val)  # создаем новый узел
        if self.end is None:  # если очередь пуста
            self.start = new_node  # новый узел становится началом очереди
            self.end = new_node  # и концом очереди
        else:
            self.end.nref = new_node  # добавляем новый узел в конец
            new_node.pref = self.end  # обновляем ссылку на предыдущий узел
            self.end = new_node  # обновляем конец очереди

    def insert(self, n, val):
        """
        Вставить элемент val между элементами с номерами n-1 и n
        """
        new_node = Node(val)
        if n <= 0:  # вставка в начало
            new_node.nref = self.start
            if self.start is not None:
                self.start.pref = new_node
            self.start = new_node
            if self.end is None:
                self.end = new_node
            return

        current = self.start
        for _ in range(n - 1):
            if current is None:  # если n больше размера очереди
                break
            current = current.nref

        if current is None:  # вставка в конец
            self.push(val)
        else:  # вставка перед текущим узлом
            new_node.nref = current
            new_node.pref = current.pref
            if current.pref is not None:
                current.pref.nref = new_node
            current.pref = new_node

            if new_node.pref is None:  # если вставляем в начало
                self.start = new_node

    def print_queue(self):
        """
        Вывод на печать содержимого очереди
        """
        current = self.start
        while current is not None:
            print(current.data)  # выводим значение текущего узла
            current = current.nref  # переходим к следующему узлу


# Пример использования очереди
queue = Queue()
queue.push(1)
queue.push(2)
queue.push(3)

print("Содержимое очереди:")
queue.print_queue()

print("Удаляем элемент:", queue.pop())
print("Содержимое очереди после удаления:")
queue.print_queue()

queue.insert(1, 4)  # Вставка 4 между 1 и 2
print("Содержимое очереди после вставки:")
queue.print_queue()