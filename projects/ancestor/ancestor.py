from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    #initiate graph and the add all values
    g = Graph()
    for i in ancestors:
        g.add_vertex(i[0])
        g.add_vertex(i[1])
    for i in ancestors:    
        g.add_edge(i[0], i[1])

    #if starting node has no parents return -1
    # if g.get_neighbors(starting_node) != g.vertices[starting_node]:
    #     return -1
    
    ###############################################
    x = g.vertices[starting_node]
    print(x.value)
    print(g.vertices[x])
    if starting_node not in g.vertices[x]:
        print('not in')
    
   


a = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

earliest_ancestor(a, 10)

