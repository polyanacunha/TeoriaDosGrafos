def get_degree(graph, vertex):
    adjacentes = graph[vertex]
    degree = len(adjacentes)
    return degree

def get_vertex_of_the_degree(graph, degree):
    answer = []
    for vertex in graph:
        degree_of_the_vertex = len(graph[vertex])
        if degree == degree_of_the_vertex:
            answer.append(vertex)
        else:
            pass
            
    return answer 

    def check_is_subgraph(graph1, graph2):
        for vertex in graph2:
            if vertex not in graph:
                return False
            else:
                adjacency_graph1 = graph1[vertex]
                adjacency_graph2 = graph2[vertex]
                for neighboor in adjacency_graph2:
                    if neighboor not in adjacency_graph1:
                        return False
                    else:
                        pass

        return True
    
def where(graph,vertex):
    return graph[vertex]

def shortest_path(graph, vertex):
    print 
    return where(graph,vertex)


    

