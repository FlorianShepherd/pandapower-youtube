# Youtube Tutorial: https://www.youtube.com/watch?v=sAHoJbfLhas
import pathlib

import matplotlib.pyplot as plt
import pandas as pd

import pandapower as pp
import pandapower.networks as nw
from pandapower import pp_dir
from pandapower.control.controller.const_control import ConstControl
from pandapower.timeseries.data_sources.frame_data import DFData
from pandapower.timeseries.output_writer import OutputWriter
from pandapower.timeseries.run_time_series import run_timeseries

# open the grid and modify it
net = nw.example_simple()
net.gen.drop(net.gen.index, inplace=True)
pp.create_sgen(net, 5, p_mw=1)

# create the data source for the controller
cigre_timeseries = pathlib.Path(pp_dir, "..", "tutorials", "cigre_timeseries_15min.json")

df = pd.read_json(cigre_timeseries)
ds = DFData(df)

# add controller for sgens and loads
ConstControl(net, "sgen", "p_mw", element_index=net.sgen.index, profile_name=["wind", "pv"], data_source=ds)
ConstControl(net, "load", "p_mw", element_index=net.load.index, profile_name=["residential"], data_source=ds)

# add the output writer to store results
ow = OutputWriter(net, time_steps=(0, 95), output_path="./results/", output_file_type=".xlsx")
# these values are logged by default anyway and must not be explicitly set
# ow.log_variable("res_bus", "vm_pu")
# ow.log_variable("res_line", "loading_percent")

# run the time series
run_timeseries(net, time_steps=range(0, 48))

# optional: plot the result
fig, axes = plt.subplots(2, 1, sharex=True)
df = pd.read_excel("./results/res_bus/vm_pu.xlsx", index_col=0)
df.plot(ax=axes[0])
axes[0].set_ylabel("bus voltage magnitude [p.u.]")
df = pd.read_excel("./results/res_line/loading_percent.xlsx", index_col=0)
df.plot(ax=axes[1])
axes[1].set_ylabel("line loading [%]")
[ax.grid() for ax in axes]
plt.xlabel("time steps")
plt.show()
