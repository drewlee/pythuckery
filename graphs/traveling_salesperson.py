import random
from shared import city_graph


def is_all_visited(visited):
    for vertex in visited:
        if not visited[vertex]:
            return False
    return True


def traveling_salesperson(graph):
    path = ""
    visited = {x: False for x in graph}
    current_vertex = random.choice(list(graph))
    visited[current_vertex] = True
    path += current_vertex
    all_visited = is_all_visited(visited)

    while not all_visited:
        current_edges = graph[current_vertex]
        current_weights = {}

        for [key, value] in current_edges:
            current_weights[key] = value

        found_next_vertex = False
        next_vertex = ""

        while not found_next_vertex:
            if not current_weights:
                break

            next_vertex = min(current_weights, key=current_weights.__getitem__)

            if visited[next_vertex]:
                current_weights.pop(next_vertex)
            else:
                found_next_vertex = True

        if not current_weights:
            all_visited = True
        else:
            current_vertex = next_vertex
            visited[current_vertex] = True
            path += " " + current_vertex

    return path


def run():
    result = traveling_salesperson(city_graph)
    print(result)


if __name__ == "__main__":
    run()
