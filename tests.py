import time
import random

from priority_queue import PriorityQueue
from protection.priority_queen_list import PriorityQueueOnUnsortedList

def test_add_order():
    queue = PriorityQueue()
    assert queue.add_order(1, "2024-12-01 10:00", 10) == True
    assert queue.add_order(1, "2024-12-01 10:00", 10) == False

def test_extract_max():
    queue = PriorityQueue()
    queue.add_order(1, "2024-12-01 10:00", 10)
    queue.add_order(2, "2024-12-01 10:30", 20)
    order = queue.extract_max()
    assert order[0] == 2

def test_peek_max():
    queue = PriorityQueue()
    queue.add_order(1, "2024-12-01 10:00", 10)
    queue.add_order(2, "2024-12-01 10:30", 20)
    order = queue.peek_max()
    assert order[0] == 2

def test_change_priority():
    queue = PriorityQueue()
    queue.add_order(1, "2024-12-01 10:00", 10)
    queue.add_order(2, "2024-12-01 10:30", 20)
    assert queue.change_priority(1, 30) == True
    order = queue.peek_max()
    assert order[0] == 1

def test_get_all_orders():
    queue = PriorityQueue()
    queue.add_order(1, "2024-12-01 10:00", 10)
    queue.add_order(2, "2024-12-01 10:30", 20)
    queue.add_order(3, "2024-12-01 11:00", 5)
    orders = queue.get_all_orders()
    assert len(orders) == 3
    assert orders[0][0] == 2

def test_boundary_values():
    queue = PriorityQueue()
    assert queue.add_order(1, "2024-12-01 10:00", 0) == True  
    assert queue.add_order(2, "2024-12-01 10:30", 100) == True 
    assert queue.add_order(3, "2024-12-01 11:00", 50) == True  
    order = queue.peek_max()
    assert order[0] == 2

def test_invalid_input():
    queue = PriorityQueue()
    try:
        queue.add_order("invalid_id", "2024-12-01 10:00", 10)
    except TypeError:
        pass
    try:
        queue.add_order(1, 12345, 10)
    except TypeError:
        pass
    try:
        queue.add_order(1, "2024-12-01 10:00", "invalid_priority")
    except TypeError:
        pass

def test_empty_queue():
    queue = PriorityQueue()
    assert queue.peek_max() is None
    assert queue.extract_max() is None

def test_large_input():
    queue = PriorityQueue()
    start_time = time.time()
    num_operations = 10000
    for i in range(num_operations):
        queue.add_order(i, "2024-12-02", i)
    for _ in range(num_operations // 2):
        queue.extract_max()
    end_time = time.time()
    print(f"test_large_input: {end_time - start_time:.2f} seconds")
    
def test_performance():
    """Тест производительности для очереди на основе кучи и неотсортированного списка"""
    sizes = [1000, 10000]
    results = {}

    for size in sizes:
        # Данные для тестирования
        test_data = [(i, random.randint(0, 1000), random.randint(0, 100)) for i in range(size)]

        # Очередь на основе кучи
        heap_queue = PriorityQueue()
        start = time.time()
        for order in test_data:
            heap_queue.add_order(order[0], order[1], order[2])
        for _ in range(size):
            heap_queue.extract_max()
        heap_time = time.time() - start

        # Очередь на основе неотсортированного списка
        list_queue = PriorityQueueOnUnsortedList()
        start = time.time()
        for order in test_data:
            list_queue.add_order(order[0], order[1], order[2])
        for _ in range(size):
            list_queue.extract_max()
        list_time = time.time() - start

        results[size] = {
            "heap_add_extract": heap_time,
            "list_add_extract": list_time,
        }

    # Результаты
    for size, times in results.items():
        print(f"Размер очереди: {size}")
        print(f"  Куча: {times['heap_add_extract']:.6f} сек")
        print(f"  Список: {times['list_add_extract']:.6f} сек")
        print()


def run_tests():
    test_add_order()
    test_extract_max()
    test_peek_max()
    test_change_priority()
    test_get_all_orders()
    test_boundary_values()
    test_invalid_input()
    test_empty_queue()
    test_large_input()
    test_performance()  

if __name__ == "__main__":
    run_tests()


