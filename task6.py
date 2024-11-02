def greedy_algorithm(items, budget):
    # Сортуємо страви за співвідношенням калорій до вартості в спадному порядку
    sorted_items = sorted(items.items(), key=lambda item: item[1]['calories'] / item[1]['cost'], reverse=True)
    
    selected_items = []
    total_cost = 0
    total_calories = 0
    
    for item, details in sorted_items:
        if total_cost + details['cost'] <= budget:
            selected_items.append(item)
            total_cost += details['cost']
            total_calories += details['calories']
    
    return selected_items, total_cost, total_calories

def dynamic_programming(items, budget):
    n = len(items)
    item_list = list(items.items())
    
    # Ініціалізація таблиці dp
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    
    # Заповнення таблиці dp
    for i in range(1, n + 1):
        item_name, item_info = item_list[i-1]
        cost = item_info["cost"]
        calories = item_info["calories"]
        
        for w in range(1, budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-cost] + calories)
            else:
                dp[i][w] = dp[i-1][w]
    
    # Відновлення оптимального набору страв
    w = budget
    selected_items = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            item_name, item_info = item_list[i-1]
            selected_items.append(item_name)
            w -= item_info["cost"]
    
    selected_items.reverse()
    return selected_items, dp[n][budget]

# Дані про їжу
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

# Задаємо бюджет
budget = 150

# Використовуємо жадібний алгоритм
selected_items, total_cost, total_calories = greedy_algorithm(items, budget)

print(f"Selected items: {selected_items}")
print(f"Total cost: {total_cost}")
print(f"Total calories: {total_calories}")

# Виклик функції dynamic_programming
selected_items, max_calories = dynamic_programming(items, budget)
print("Вибрані страви:", selected_items)
print("Максимальна калорійність:", max_calories)