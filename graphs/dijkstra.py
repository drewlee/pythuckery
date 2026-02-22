from heapq import heappop, heappush
from shared import city_graph


def dijkstras(graph, start):
    distances = {}
    paths = {}

    for vertex in graph:
        distances[vertex] = float("inf")

    distances[start] = 0
    vertices = [(0, start)]
    paths[start] = [start]

    while vertices:
        distance, current = heappop(vertices)

        for neighbor, weight in graph[current]:
            new_distance = distance + weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                paths[neighbor] = paths[current] + [neighbor]
                heappush(vertices, (new_distance, neighbor))

    print(paths)

    return distances


def run():
    graph = {
        "A": [("B", 10), ("C", 3)],
        "C": [("D", 2)],
        "D": [("E", 10)],
        "E": [("A", 7)],
        "B": [("C", 3), ("D", 2)],
    }

    result = dijkstras(graph, "D")
    print(f"Shortest Distances: {result}")

    result = dijkstras(city_graph, "a")
    print(f"Shortest Distances: {result}")


if __name__ == "__main__":
    run()
