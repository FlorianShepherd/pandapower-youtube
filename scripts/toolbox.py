# Youtube Tutorial: https://www.youtube.com/watch?v=O74yw1FmmsM
import pandapower.toolbox as tb
import pandapower.networks as nw
import pandapower as pp

net = nw.create_cigre_network_mv()
pp.runpp(net)
# print some power flow information
tb.lf_info(net)

net2 = nw.create_cigre_network_mv()
net2.load.drop(index=0, inplace=True)
# check if two nets are identical. You can also only check the results
tb.nets_equal(net, net2)

# merge two power systems
net3 = tb.merge_nets(net, net2)
# drop some buses
tb.drop_buses(net, buses=[5])
# creates a continuous index in net.bus starting at 10
tb.create_continuous_bus_index(net, start=10)

# get all line elements connected to buses
els = tb.get_connected_elements(net, "line", buses=[11])
print(els)
print(net.line.loc[els])