# Youtube Tutorial https://www.youtube.com/watch?v=yEIsUHyTY04
import pandapower.networks as nw
import pandapower as pp
import pandapower.control as ct

net = nw.mv_oberrhein()
ct.ContinuousTapControl(net, 114, 0.99, 1e-5)
# ct.DiscreteTapControl(net, 114, 0.99, 1.01)
pp.runpp(net, run_control=True)

print(net.trafo.tap_pos)
print(net.res_bus.loc[net.trafo.lv_bus, "vm_pu"])
