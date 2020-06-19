# YouTube Tutorial: https://www.youtube.com/watch?v=p8re_RzmlbU
import pandapower.estimation as est
import pandapower as pp

net = pp.create_empty_network()

b1 = pp.create_bus(net, name="bus 1", vn_kv=1., index=1)
b2 = pp.create_bus(net, name="bus 2", vn_kv=1., index=2)
b3 = pp.create_bus(net, name="bus 3", vn_kv=1., index=3)

pp.create_ext_grid(net, b1)  # set the slack bus to bus 1

l1 = pp.create_line_from_parameters(net, 1, 2, 1, r_ohm_per_km=.01, x_ohm_per_km=.03, c_nf_per_km=0., max_i_ka=1)
l2 = pp.create_line_from_parameters(net, 1, 3, 1, r_ohm_per_km=.02, x_ohm_per_km=.05, c_nf_per_km=0., max_i_ka=1)
l3 = pp.create_line_from_parameters(net, 2, 3, 1, r_ohm_per_km=.03, x_ohm_per_km=.08, c_nf_per_km=0., max_i_ka=1)

# bus voltages
pp.create_measurement(net, "v", "bus", 1.006, 0.004, b1)
pp.create_measurement(net, "v", "bus", .968, 0.004, b2)

# bus, p, q
pp.create_measurement(net, "p", "bus", -0.501, 10., b2)
pp.create_measurement(net, "q", "bus", -.266, 10., b2)

# line
pp.create_measurement(net, "p", "line", 0.888, 8., l1, side=1)
pp.create_measurement(net, "p", "line", 1.173, 8., l2, side=1)
pp.create_measurement(net, "q", "line", 0.568, 8., l1, side=1)
pp.create_measurement(net, "q", "line", 0.663, 8., l2, side=1)

est.estimate(net)

print(net.res_bus_est)
print(net.res_line_est)