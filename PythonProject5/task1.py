class Node:
    """
    Вспомогательный класс для узлов списка
    """

    def __init__(self, data):
        self.data = data  # храним информацию
        self.pref = None  # ссылка на предыдущий узел


class Stack:
    """
    Основной класс для стека
    """

    def __init__(self):
        self.end = None  # ссылка на конец стека

    def pop(self):
        """
        Возвращение последнего элемента из списка с удалением его из списка
        """
        if self.end is None:
            raise IndexError("pop from empty stack")

        val = self.end.data  # сохраняем значение последнего элемента
        self.end = self.end.pref  # перемещаем указатель на предыдущий элемент
        return val  # возвращаем значение

    def push(self, val):
        """
        Добавление элемента val в конец списка
        """
        new_node = Node(val)  # создаем новый узел
        new_node.pref = self.end  # новый узел указывает на текущий конец стека
        self.end = new_node  # обновляем конец стека

    def print_stack(self):
        """
        Вывод на печать содержимого стека
        """
        current = self.end
        while current is not None:
            print(current.data)  # выводим значение текущего узла
            current = current.pref  # переходим к предыдущему узлу


# Пример использования стека
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print("Содержимое стека:")
stack.print_stack()

print("Удаляем элемент:", stack.pop())
print("Содержимое стека после удаления:")
stack.print_stack()