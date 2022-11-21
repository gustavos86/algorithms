"""
Chapter 18
Connecting Everything with Graphs

Exercises
The following exercises provide you with the opportunity to practice with graphs.
"""
from queue import Queue

class Vertex:
    def __init__(self, value):
        self.value = value
        self.adjacent_vertices = []

    def add_adjacent_vertex(self, vertex):
        self.adjacent_vertices.append(vertex)


def question4():
    """
    In this chapter, I only provided the code for breadth-first traversal, as discussed in Breadth-First Search.
    That is, the code simply printed the value of each vertex.
    Modify the code so that it performs an actual search for a vertex value provided to the function.
    (We did this for depth-first search.)
    That is, if the function finds the vertex it's searching for, it should return that vertex's value.
    Otherwise, it should return null
    """
    def bfs_lookup(source_vertex, vertex_to_find):
        queue = Queue()
      
        visited_vertices = {}
        visited_vertices[source_vertex.value] = True
        queue.put(source_vertex)
      
        # While the queue is not empty:​
        while queue.qsize():
      
            # Remove the first vertex off the queue and make it the current vertex:​
            current_vertex = queue.get()
      
            # Print the current vertex's value:​
            print(current_vertex.value, end=" ")
            if current_vertex.value == vertex_to_find.value:
                return current_vertex.value

            # Iterate over current vertex's adjacent vertices:​
            for adjacent_vertex in current_vertex.adjacent_vertices:
      
                # If we have not yet visited the adjacent vertex:​
                if not visited_vertices.get(adjacent_vertex.value):

                    # Mark the adjacent vertex as visited:​
                    visited_vertices[adjacent_vertex.value] = True

                    # Add the adjacent vertex to the queue:​
                    queue.put(adjacent_vertex)

        # Vertex not found
        return None
    ###############
    A = Vertex("A")
    B = Vertex("B")
    C = Vertex("C")
    D = Vertex("D")
    E = Vertex("E")
    F = Vertex("F")
    G = Vertex("G")
    H = Vertex("H")
    I = Vertex("I")
    J = Vertex("J")
    K = Vertex("K")
    L = Vertex("L")
    M = Vertex("M")
    N = Vertex("N")
    O = Vertex("O")
    P = Vertex("P")

    Z = Vertex("Z")

    A.add_adjacent_vertex(B)
    A.add_adjacent_vertex(C)
    A.add_adjacent_vertex(D)

    B.add_adjacent_vertex(E)
    B.add_adjacent_vertex(F)

    E.add_adjacent_vertex(J)
    F.add_adjacent_vertex(J)

    J.add_adjacent_vertex(O)

    C.add_adjacent_vertex(G)
    G.add_adjacent_vertex(K)

    D.add_adjacent_vertex(H)
    D.add_adjacent_vertex(I)

    H.add_adjacent_vertex(L)
    H.add_adjacent_vertex(M)

    I.add_adjacent_vertex(M)
    I.add_adjacent_vertex(N)
    N.add_adjacent_vertex(P)

    vertex_to_find = O
    if found := bfs_lookup(A, vertex_to_find):
        print(f"\nBFS found vertex: {found}")
    else:
        print(f"\nBFS did not found vertex: {vertex_to_find.value}")

def question5():
    """
    In Dijkstra's Algorithm, we saw how Dijkstra's algorithm helped us find the shortest path within a weighted graph.
    However, the concept of a shortest path exists within an unweighted graph as well. How?
    
    The shortest path in a classic (unweighted) graph is the path that takes the fewest number of vertices to get from one vertex to another.
    This can be especially useful in social networking applications. Take the example network that follows:
    
    If we want to know how Idris is to connected Lina, we'd see that she's connected to her from two different directions.
    That is, Idris is a second-degree connection to Lina through Kamil, but she is also a fifth-degree connection through Talia.
    Now, we're probably interested in how closely Idris is connected to Lina,
    so the fact that she's a fifth-degree connection is unimportant given that they're also second-degree connections.
    
    Write a function that accepts two vertices from a graph and returns the shortest path between them.
    The function should return an array containing the precise path, such as ["Idris", "Kamil", "Lina"].
    
    Hint: The algorithm may contain elements of both breadth-first search and Dijkstra's algorithm.
    """
    def dijkstra_shortest_path(source_vertex, destination_vertex):
        shortest_path_table = {}
        shortest_previous_middle_path_table = {}
    
        # To keep our code simple, we'll use a basic array to keep track of
        # the known cities we haven't yet visited:
        unvisited_vertex = []
    
        # We keep track of the cities we've visited using a hash table. 
        # We could have used an array, but since we'll be doing lookups,
        # a hash table is more efficient:
        visited_vertex = {}
    
        # We add the starting city's name as the first key inside the 
        # shortest_path_table. It has a value of 0, since it costs nothing
        # to get there:
        shortest_path_table[source_vertex.value] = 0
    
        current_vertex = source_vertex
    
        # This loop is the core of the algorithm. It runs as long as we can 
        # visit a city that we haven't visited yet:
        while current_vertex:
    
            # We add the current_vertex's name to the visited_vertex hash to record
            # that we've officially visited it. We also remove it from the list
            # of unvisited cities:
            visited_vertex[current_vertex.value] = True
            if current_vertex in unvisited_vertex:
                unvisited_vertex.remove(current_vertex)
    
            # We iterate over each of the current_vertex's adjacent cities:
            for adjacent_vertexs in current_vertex.adjacent_vertices:
    
                # If we've discovered a new city, 
                # we add it to the list of unvisited_vertex:
                if not visited_vertex.get(adjacent_vertexs.value):
                    unvisited_vertex.append(adjacent_vertexs)

                    # We calculate the price of getting from the STARTING city to the
                    # ADJACENT city using the CURRENT city as the second-to-last stop:
                    price_through_current_city = shortest_path_table[current_vertex.value] + 1
            
                    # If the price from the STARTING city to the ADJACENT city is 
                    # the cheapest one we've found so far...
                    if not shortest_path_table.get(adjacent_vertexs.value) or price_through_current_city < shortest_path_table[adjacent_vertexs.value]:

                        # ... we update our two tables:
                        shortest_path_table[adjacent_vertexs.value] = price_through_current_city
                        shortest_previous_middle_path_table[adjacent_vertexs.value] = current_vertex.value

            # We visit our next unvisited city. We choose the one that is cheapest
            # to get to from the STARTING city:
            if unvisited_vertex:
                current_vertex = unvisited_vertex[0]
                for vertex in unvisited_vertex:
                    if shortest_path_table[vertex.value] < shortest_path_table[current_vertex.value]:
                        current_vertex = vertex
            else:
                current_vertex = None
            
    
        # We have completed the core algorithm. At this point, the
        # shortest_path_table contains all the cheapest prices to get to each
        # city from the starting city. However, to calculate the precise path
        # to take from our starting city to our final destination, we need to move on.
        
        # We'll build the shortest path using a simple array:
        shortest_path = []
      
        # To construct the shortest path, we need to work backwards from our 
        # final destination. So we begin with the final destination as our 
        # current_vertex_value:
        current_vertex_value = destination_vertex.value
    
        # We loop until we reach our starting city:
        while current_vertex_value != source_vertex.value:
    
            # We add each current_vertex_value we encounter to the shortest path array:
            shortest_path.append(current_vertex_value)
            # We use the shortest_previous_middle_path_table to follow each city
            # to its previous stopover city:
            current_vertex_value = shortest_previous_middle_path_table[current_vertex_value]

        
        # We cap things off by adding the starting city to the shortest path:
        shortest_path.append(source_vertex.value)
        
        # We reverse the output so we can see the path from beginning to end:
        shortest_path.reverse()
        return shortest_path

    A = Vertex("A")
    B = Vertex("B")
    C = Vertex("C")
    D = Vertex("D")
    E = Vertex("E")
    F = Vertex("F")
    G = Vertex("G")
    H = Vertex("H")
    I = Vertex("I")
    J = Vertex("J")
    K = Vertex("K")
    L = Vertex("L")
    M = Vertex("M")
    N = Vertex("N")
    O = Vertex("O")
    P = Vertex("P")

    Z = Vertex("Z")

    A.add_adjacent_vertex(B)
    A.add_adjacent_vertex(C)
    A.add_adjacent_vertex(D)

    B.add_adjacent_vertex(E)
    B.add_adjacent_vertex(F)

    E.add_adjacent_vertex(J)
    F.add_adjacent_vertex(J)

    J.add_adjacent_vertex(O)  # ['A', 'D', 'I', 'N', 'P', 'O'] if commented. A to O

    C.add_adjacent_vertex(G)
    G.add_adjacent_vertex(K)

    D.add_adjacent_vertex(H)
    D.add_adjacent_vertex(I)

    H.add_adjacent_vertex(L)
    H.add_adjacent_vertex(M)

    I.add_adjacent_vertex(M)
    I.add_adjacent_vertex(N)
    #N.add_adjacent_vertex(P)

    P.add_adjacent_vertex(O)
    O.add_adjacent_vertex(P)

    source_vertex      = A
    destination_vertex = P
    #if shortest_path := find_shortest_path(source_vertex, destination_vertex):
    if shortest_path := dijkstra_shortest_path(source_vertex, destination_vertex):
        print(f"\nThe Shortest path between {source_vertex.value} and {destination_vertex.value} is {shortest_path}")


#question4()
question5()