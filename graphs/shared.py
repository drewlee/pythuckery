# Graph for traveling salesperson problem.
city_graph = {
    "a": [("b", 3), ("c", 4), ("d", 5)],
    "b": [("a", 3), ("c", 2), ("d", 6)],
    "c": [("a", 4), ("b", 2), ("d", 1)],
    "d": [("a", 5), ("b", 6), ("c", 1)],
}
