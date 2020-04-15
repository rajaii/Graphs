# Write a function that takes a 2D binary array and returns 
# the number of 1 islands. An island consists of 1s that are 
# connected to the north, south, east or west. For example:
# islands = [[0, 1, 0, 1, 0],
#            [1, 1, 0, 1, 1],
#            [0, 0, 1, 0, 0],
#            [1, 0, 1, 0, 0],
#            [1, 1, 0, 0, 0]]
# island_counter(islands) # returns 4

#islands consist of - connected components
#connected - neighbors (edges)
#directions, new (edges)
#2d array - graph, more or less
#returns (shape of solution) - number of islands

#How could we write a get neighbor function that uses this shape?
#offset coordinates

#how can we find the extent of an island?
#Either traversals to find all nodes in an island

#How do I explore the larger set?
#Loop through and call the traversal if we find an unvisited 1