# Youtube Tutorial: https://www.youtube.com/watch?v=O99JNoUytAc&t=1s
import pandapower as pp
import pandapower.networks as nw
import pandapower.plotting as pplt

# get the power system
net = nw.mv_oberrhein()

# use matplotlib
pplt.simple_plot(net)

# use plotly (install plotly first with 'pip install plotly')
pplt.simple_plotly(net)