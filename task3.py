import heapq

def dijkstra(graph, start):
    # Ініціалізація відстаней та множини невідвіданих вершин
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = [(0, start)]

    while unvisited:
        # Знаходження вершини з найменшою відстанню серед невідвіданих
        current_distance, current_vertex = heapq.heappop(unvisited)

        # Якщо ця відстань до вершини більше, ніж збережене, то ігноруємо
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight

            # Якщо нова відстань коротша, то оновлюємо найкоротший шлях
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(unvisited, (distance, neighbor))

    return distances

# Приклад графа у вигляді словника
graph = {
    'A': {'B': 5, 'C': 10},
    'B': {'A': 5, 'D': 3},
    'C': {'A': 10, 'D': 2},
    'D': {'B': 3, 'C': 2, 'E': 4},
    'E': {'D': 4}
}

# Виклик функції для вершини A
print(dijkstra(graph, 'A'))
