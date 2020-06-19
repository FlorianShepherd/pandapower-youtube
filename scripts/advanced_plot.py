# YouTube Tutorial: https://www.youtube.com/watch?v=4LQLZQWPaPM
import pandapower.networks as nw
import pandapower.plotting as plot
import matplotlib.pyplot as plt
import seaborn

colors = seaborn.color_palette()

net = nw.mv_oberrhein()
bc = plot.create_bus_collection(net, buses=net.bus.index, color=colors[0], size=80, zorder=1)
lc = plot.create_line_collection(net, lines=net.line.index, color='grey', zorder=2)

long_lines = net.line.loc[net.line.length_km > 2.].index
lcl = plot.create_line_collection(net, lines=long_lines, color=colors[2], zorder=2)
plot.draw_collections([lc, bc, lcl])
plt.show()
