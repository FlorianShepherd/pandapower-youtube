# Youtube Tutorial: https://www.youtube.com/watch?v=9qbrt_uPkJw
import pandapower as pp
import pandapower.networks as nw

# get the power system
net = nw.simple_four_bus_system()
# print some information about the pandas DataFrames
print(net)
# run the power flow
pp.runpp(net)
# the print now includes some information about the results
print(net)
# you can print detailed information for every element
print(net.bus)
print(net.res_bus)
