import networkx as nx

import evolgamenet as eg




#g=nx.random_geometric_graph(100,0.03)

rslt=eg.evol_game_fiv(100,0.046,1.2,1,0,0.1,1000)

#print rslt[0]


nx.write_gml(rslt[1],'evol_graph.gml')
