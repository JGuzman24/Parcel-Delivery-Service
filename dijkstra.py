# Dijkstra shortest path
def dijkstra_shortest_path(g, start_vertex):
    # Put all vertices in an unvisited queue.
    unvisited_queue = []

    for current_vertex in g.adjacency_list:
        unvisited_queue.append(current_vertex)
        # unvisited_queue = [vertex_1, vertex_2, ...]



    # Start_vertex has a distance of 0 from itself
    start_vertex.distance = 0
    package = 0
    # One vertex is removed with each iteration; repeat until the list is
    # empty.
    while len(unvisited_queue) > 0:
        # Visit vertex with minimum distance from start_vertex
        smallest_index = 0

        for i in range(1, len(unvisited_queue)):
            # print(unvisited_queue[i].label, unvisited_queue[i].distance, unvisited_queue[i].pred_vertex)
            if unvisited_queue[i].distance < unvisited_queue[smallest_index].distance:
                smallest_index = i
        current_vertex = unvisited_queue.pop(smallest_index)
        #print("From Start ({}) to Current ({}): ".format(start_vertex.label,current_vertex.label) +" distance: " + str(current_vertex.distance))

        # Check potential path lengths from the current vertex to all neighbors.
        for adj_vertex in g.adjacency_list[current_vertex]:  # values from  dictionary
            # if current_vertex = vertex_1 => adj_vertex in [vertex_2, vertex_3], if vertex_2 => adj_vertex in [vertex_6], ...
            edge_weight = g.edge_weights[(current_vertex, adj_vertex)]  # values from dictionary
            # edge_weight = 484 then 626 then 1306, ...}
            alternative_path_distance = current_vertex.distance + float(edge_weight)

            # If shorter path from start_vertex to adj_vertex is found, update adj_vertex's distance and predecessor
            if alternative_path_distance < adj_vertex.distance:
                adj_vertex.distance = alternative_path_distance
                adj_vertex.pred_vertex = current_vertex


def get_shortest_path(start_vertex, end_vertex):
    # Start from end_vertex and build the path backwards.
    path = []
    current_vertex = end_vertex
    print("Begin: " + start_vertex.label)
    print("End: " + end_vertex.label)
    print("Current: " + end_vertex.pred_vertex.label)

    while current_vertex is not start_vertex:
        print("While")
        path.insert(0, str(current_vertex.label))
        if current_vertex.pred_vertex != None:
            current_vertex = current_vertex.pred_vertex
            print("Current: " + current_vertex.label)
        else:
            print("ending")
            break
        print("Cancel")
        print(path)
    start_vertex.pred_vertex = None

    return path
