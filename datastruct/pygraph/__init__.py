import networkx as nx
import matplotlib.pyplot as plt

E = [('r', 's'), ('r', 'v'), ('s', 'r'), ('s', 'w'), ('t', 'w'), ('t', 'x'), ('t', 'u'), ('u','t'), ('u', 'x')]
G = nx.Graph(E)
G.edges[1, 2]['color'] = 'red'
G.add_edge(2, 4)
a = nx.bfs_tree(G, 1)


#nx.draw(G, with_labels=True, font_weight='bold')
#plt.show()
