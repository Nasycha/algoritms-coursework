from priority_queue import PriorityQueue

def print_menu():
    print("\033[94m" + "-" * 40)
    print("📋 Меню:")
    print("1. Добавить заказ")
    print("2. Извлечь заказ с максимальным приоритетом")
    print("3. Посмотреть заказ с максимальным приоритетом")
    print("4. Изменить приоритет заказа")
    print("5. Посмотреть все заказы")
    print("6. Визуализировать очередь")
    print("7. Выход")
    print("-" * 40 + "\033[0m")

def main():
    queue = PriorityQueue()
    while True:
        print_menu()
        choice = input("\033[93mВведите номер действия: \033[0m")
        if choice == "1":
            order_id = int(input("Введите ID заказа: "))
            arrive_time = input("Введите время прибытия: ")
            priority = int(input("Введите приоритет: "))
            if queue.add_order(order_id, arrive_time, priority):
                print("\033[92mЗаказ успешно добавлен.\033[0m")
            else:
                print("\033[91mОшибка: заказ с таким ID уже существует.\033[0m")
        elif choice == "2":
            order = queue.extract_max()
            if order:
                print(
                    f"📦 Order Details:\n"
                    f"   🆔 ID: {order[0]}\n"
                    f"   ⏰ Time: {order[1]}\n"
                    f"   🔝 Priority: {order[2]}\n")
            else:
                print("\033[91mОчередь пуста.\033[0m")

        elif choice == "3":
            order = queue.peek_max()
            if order:
                print(
                    f"📦 Order Details:\n"
                    f"   🆔 ID: {order[0]}\n"
                    f"   ⏰ Time: {order[1]}\n"
                    f"   🔝 Priority: {order[2]}\n")
            else:
                print("\033[91mОчередь пуста.\033[0m")
        elif choice == "4":
            order_id = int(input("Введите ID заказа: "))
            new_priority = int(input("Введите новый приоритет: "))
            if queue.change_priority(order_id, new_priority):
                print("\033[92mПриоритет изменён.\033[0m")
            else:
                print("\033[91mОшибка: заказ не найден.\033[0m")
        elif choice == "5":
            for order in queue.get_all_orders():
                print(
                    f"📦 Order Details:\n"
                    f"   🆔 ID: {order[0]}\n"
                    f"   ⏰ Time: {order[1]}\n"
                    f"   🔝 Priority: {order[2]}\n")
        elif choice == "6":
            queue.visualize()
        elif choice == "7":
            print("\033[92mВыход.\033[0m")
            break
        else:
            print("\033[91mНеверный выбор.\033[0m")


if __name__ == "__main__":
    main()


# 1, "2024-12-01 10:00", 10
# 2, "2024-12-01 10:30", 20
# 3, "2024-12-01 11:00", 5
# 4, "2024-12-01 12:00", 1

