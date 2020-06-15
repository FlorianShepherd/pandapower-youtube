# Youtube Tutorial: https://www.youtube.com/watch?v=66SSDhSNV7k
import pandapower as pp
import pandapower.shortcircuit as sc

def ring_network():
    net = pp.create_empty_network()
    b1 = pp.create_bus(net, 220)
    b2 = pp.create_bus(net, 110)
    b3 = pp.create_bus(net, 110)
    b4 = pp.create_bus(net, 110)

    pp.create_ext_grid(net, b1, s_sc_max_mva=100., s_sc_min_mva=80., rx_min=0.20, rx_max=0.35)

    pp.create_transformer(net, b1, b2, "100 MVA 220/110 kV")
    pp.create_line(net, b2, b3, std_type="N2XS(FL)2Y 1x120 RM/35 64/110 kV", length_km=15.)
    l2 = pp.create_line(net, b3, b4, std_type="N2XS(FL)2Y 1x120 RM/35 64/110 kV", length_km=12.)
    pp.create_line(net, b4, b2, std_type="N2XS(FL)2Y 1x120 RM/35 64/110 kV", length_km=10.)
    pp.create_switch(net, b4, l2, closed=False, et="l")
    return net

net = ring_network()
net.switch.loc[:, "closed"] = True
sc.calc_sc(net, ith=True, ip=True, tk_s=2., branch_results=True, topology="auto")
print(net.res_bus_sc)
print(net.res_line_sc)