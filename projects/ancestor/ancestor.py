from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    #initiate graph and the add all values
    g = Graph()
    for i in ancestors:
        g.add_vertex(i[0])
        g.add_vertex(i[1])
    for i in ancestors:    
        g.add_edge(i[0], i[1])
    # #####################################
    # count = 0
    # for i in g.vertices:
    #     if starting_node not in g.vertices[i]:
    #         count += 0
    # ######################
    # new_count = 1
    # if count > 0:
    #     new_count = count        
    # if new_count == 0:
    #     return -1        
    # ######################### 
    ######################################################
    #flip the chabang around and traverse other direction
    n_g = Graph()
    for i in ancestors:
        n_g.add_vertex(i[0])
        n_g.add_vertex(i[1])
    for i in ancestors:    
        n_g.add_edge(i[1], i[0])
    if n_g.dft(starting_node) == starting_node:
        return -1   
    return n_g.dft(starting_node)
    

    
    

    
   


a = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(a, 8))

