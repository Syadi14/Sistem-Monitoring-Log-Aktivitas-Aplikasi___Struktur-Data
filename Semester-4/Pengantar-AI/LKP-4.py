import aima3.search as s

indo_graph = s.UndirectedGraph(
    dict(
        Bekasi=dict(Karawang=10, Bogor=10),
        Karawang=dict(Bekasi=10, Purwakarta=8, Subang=8),
        Subang=dict(Karawang=8, Purwakarta=8, Sumedang=10, Indramayu=10),
        Bogor=dict(Bekasi=10, Sukabumi=15, Cianjur=8),
        Bandung=dict(West_Bandung=5, Garut=8, Cianjur=8, Sumedang=10),
        Tasikmalaya=dict(Garut=8, Pangandaran=8, Ciamis=5),
        Ciamis=dict(Tasikmalaya=5, Pangandaran=5, Kuningan=8),
        Majalengka=dict(Kuningan=10, Sumedang=5),
        Sumedang=dict(Majalengka=5, Subang=10, Bandung=10),
        Purwakarta=dict(Karawang=8, Subang=8, Cianjur=8),
        Sukabumi=dict(Bogor=15, Cianjur=15),
        Cianjur=dict(Sukabumi=15, Purwakarta=8, Bandung=8, Bogor=8, West_Bandung=8),
        West_Bandung=dict(Cianjur=8, Bandung=5),
        Garut=dict(Tasikmalaya=8, Bandung=8),
        Pangandaran=dict(Tasikmalaya=8, Ciamis=5),
        Kuningan=dict(Majalengka=10, Ciamis=8, Cirebon=8),
        Cirebon=dict(Kuningan=8, Indramayu=8),
        Indramayu=dict(Cirebon=8, Subang=10),
    )
)

indo_graph.locations = dict(
    Bekasi=(10.0, 50.0),
    Karawang=(20.0, 50.0),
    Subang=(20.0, 40.0),
    Bogor=(20.0, 30.0),
    Bandung=(30.0, 10.0),
    Tasikmalaya=(45.0, 5.0),
    Ciamis=(50.0, 20.0),
    Majalengka=(40.0, 20.0),
    Sumedang=(35.0, 25.0),
    Purwakarta=(30.0, 30.0),
    Sukabumi=(20.0, 20.0),
    Cianjur=(23.0, 20.0),
    West_Bandung=(25.0, 10.0),
    Garut=(40.0, 5.0),
    Pangandaran=(50.0, 5.0),
    Kuningan=(45.0, 20.0),
    Cirebon=(45.0, 30.0),
    Indramayu=(40.0, 30.0),
)

indo_problem = s.GraphProblem("Bogor", "Pangandaran", indo_graph)
heuristic = indo_problem.h

print("Bogor ke Pangandaran Problem:")


best_first_node = s.best_first_graph_search(indo_problem, heuristic) #---- best_first_node
astar_node = s.astar_search(indo_problem, heuristic) #-------------------- astar_node


print(f"Best First Search: Bogor -> {' -> '.join(best_first_node.solution())}\nCost: {best_first_node.path_cost}") #-- best_first_node
print(f"A* Search: Bogor -> {' -> '.join(astar_node.solution())}\nCost: {astar_node.path_cost}") #-------------------- astar_node