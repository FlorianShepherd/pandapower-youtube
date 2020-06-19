# YouTube Tutorial: https://www.youtube.com/watch?v=ubpHrrMA63A
import pandapower.networks as nw
import pandapower.topology as top
import networkx as nx

net = nw.simple_mv_open_ring_net()
mg = top.create_nxgraph(net)
shortest = nx.shortest_path(mg, 0, 5)
print(shortest)
