'''
dijkstra from lecture
'''
# O(N) + # O(NlogN)
def dijkstra_shortest_path(g, start_vertex):
    # Put all vertices in an unvisited queue.
    unvisited_queue = []

    # O(N)
    for current_vertex in g.adjacency_list:
        unvisited_queue.append(current_vertex)
        # unvisited_queue = [vertex_1, vertex_2, ...]

    start_vertex.distance = 0
    package = 0

    # O(logN)
    while len(unvisited_queue) > 0:
        # Visit vertex with minimum distance from start_vertex
        smallest_index = 0

        # O(N)
        for i in range(1, len(unvisited_queue)):
            if unvisited_queue[i].distance < unvisited_queue[smallest_index].distance:
                smallest_index = i
        current_vertex = unvisited_queue.pop(smallest_index)

        # O(N)
        for adj_vertex in g.adjacency_list[current_vertex]:  # values from  dictionary
            edge_weight = g.edge_weights[(current_vertex, adj_vertex)]  # values from dictionary
            alternative_path_distance = current_vertex.distance + float(edge_weight)

            if alternative_path_distance < adj_vertex.distance:
                adj_vertex.distance = alternative_path_distance
                adj_vertex.pred_vertex = current_vertex


'''
Modified from lecture to add vertex into a list instead of string
'''
# (logN)
def get_shortest_path(start_vertex, end_vertex):
    # Start from end_vertex and build the path backwards.
    path = []
    current_vertex = end_vertex
    while current_vertex is not start_vertex and current_vertex is not None:
        path.insert(0, current_vertex)
        current_vertex = current_vertex.pred_vertex
    return path
