# Youtube Tutorial: https://www.youtube.com/watch?v=QYDp_-TX7C4
import pandapower as pp
import pandapower.plotting as pplt
import pandapower.topology as top
import pandapower.networks as nw
import matplotlib.pyplot as plt
import seaborn as sns

net = nw.mv_oberrhein()
pplt.simple_plot(net)

mg = top.create_nxgraph(net, nogobuses=set(net.trafo.lv_bus.values) | set(net.trafo.hv_bus.values))
colors = sns.color_palette()
collections = list()
sizes = pplt.get_collection_sizes(net)
for area, color in zip(top.connected_components(mg), colors):
    collections.append(pplt.create_bus_collection(net, area, color=color, size=sizes["bus"]))
    line_ind = net.line.loc[:, "from_bus"].isin(area) | net.line.loc[:, "to_bus"].isin(area)
    lines = net.line.loc[line_ind].index
    collections.append(pplt.create_line_collection(net, lines, color=color))
collections.append(pplt.create_ext_grid_collection(net, size=sizes["ext_grid"]))
pplt.draw_collections(collections)
plt.show()