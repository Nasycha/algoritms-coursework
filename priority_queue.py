import matplotlib.pyplot as plt

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def _heapify_up(self, index):
        """Для добавления элемента в кучу (добавляем вниз и провеиваем вверх)"""
        parent = (index - 1) // 2
        if index > 0 and self.heap[index][2] > self.heap[parent][2]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)

    def _heapify_down(self, index):
        """Для извлечения максимального элемента из кучи (перемещаем последний элемент на место корня и провеиваем вниз)"""
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index

        if left < len(self.heap) and self.heap[left][2] > self.heap[largest][2]:
            largest = left
        if right < len(self.heap) and self.heap[right][2] > self.heap[largest][2]:
            largest = right

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

    def add_order(self, order_id, arrive_time, priority):
        """Добавляет новый заказ в очередь"""
        # Проверка на существующий ID
        for order in self.heap:
            if order[0] == order_id:
                return False # Возвращаем False, если заказ с таким ID уже существует
        order = (order_id, arrive_time, priority)
        self.heap.append(order)
        self._heapify_up(len(self.heap) - 1)
        return True # Возвращаем True, если заказ успешно добавлен

    def extract_max(self):
        """Извлекает заказ с максимальным приоритетом"""
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0] # максимальный элемент
        # Перемещаем последний элемент на место корня
        last_element = self.heap.pop()
        self.heap[0] = last_element
        self._heapify_down(0)
        return root

    def peek_max(self):
        """Возвращает заказ с максимальным приоритетом без удаления"""
        return self.heap[0] if self.heap else None

    def change_priority(self, order_id, new_priority):
        """Изменяет приоритет существующего заказа"""
        for i, order in enumerate(self.heap):
            if order[0] == order_id:
                old_priority = order[2]
                self.heap[i] = (order[0], order[1], new_priority)
                if new_priority > old_priority:
                    self._heapify_up(i)  # Если новый приоритет больше старого, проверяем вверх
                else:
                    self._heapify_down(i)  # Если новый приоритет меньше старого, проверяем вниз
                return True # Возвращаем True, если приоритет изменён

        return False # Возвращаем False, если заказ не найден

    def get_all_orders(self):
        """Возвращает все заказы в порядке убывания приоритета"""
        return sorted(self.heap, key=lambda x: x[2], reverse=True)

    def visualize(self):
        """Визуализирует очередь в виде двоичного дерева с помощью matplotlib"""
        def plot_tree(index, x, y, dx):
            """Рекурсивная отрисовка узлов и их связей"""
            if index >= len(self.heap):
                return

            # Отображение текущего узла
            ax.text(x, y, f"ID: {self.heap[index][0]}\nPriority: {self.heap[index][2]}",
                    ha='center', va='center', bbox=dict(facecolor='white', edgecolor='black'))

            # Левый дочерний элемент
            left = 2 * index + 1
            if left < len(self.heap):
                ax.plot([x, x - dx], [y, y - 1], 'k-')  # Линия к левому дочернему узлу
                plot_tree(left, x - dx, y - 1, dx / 2)

            # Правый дочерний элемент
            right = 2 * index + 2
            if right < len(self.heap):
                ax.plot([x, x + dx], [y, y - 1], 'k-')  # Линия к правому дочернему узлу
                plot_tree(right, x + dx, y - 1, dx / 2)

        if not self.heap:
            print("Очередь пуста.")
            return

        # Настройка графика
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.axis('off')

        # Запуск рекурсивной функции отрисовки с корня дерева
        plot_tree(0, 0.5, 1, 0.25)

        # Показ графика
        plt.show()
