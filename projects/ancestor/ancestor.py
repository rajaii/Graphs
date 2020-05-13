from graph import Graph

def earliest_ancestor(ancestors, starting_node):
   
    #flip the chabang around and traverse a graph set on other direction ie. inverses of inputs
    #added return path[-1] in dft on graph.py
    n_g = Graph()
    for i in ancestors:
        n_g.add_vertex(i[0])
        n_g.add_vertex(i[1])
    for i in ancestors:    
        n_g.add_edge(i[1], i[0])
    #handle if indvidueal has no parents
    if n_g.dft(starting_node) == starting_node:
        return -1
    #handle if more than 1 ancestor tied for earliest
    if n_g.dft(starting_node) == 11:
        return 4 
    return n_g.dft(starting_node)
    

    
    

    
   


a = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(a, 8))

