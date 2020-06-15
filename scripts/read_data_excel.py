# Youtube Tutorial: https://www.youtube.com/watch?v=QeOrLzb9T8o
import pandas as pd
import pandapower as pp

net = pp.create_empty_network()
df = pd.read_excel("read_data_excel.xlsx", sheet_name="bus", index_col=0)
for idx in df.index:
    pp.create_bus(net, vn_kv=df.at[idx, "vn_kv"])

df = pd.read_excel("read_data_excel.xlsx", sheet_name="load", index_col=0)
for idx in df.index:
    pp.create_load(net, bus=df.at[idx, "bus"], p_mw=df.at[idx, "p"])

df = pd.read_excel("read_data_excel.xlsx", sheet_name="slack", index_col=0)
for idx in df.index:
    pp.create_ext_grid(net, bus=df.at[idx, "bus"], vm_pu=df.at[idx, "vm_pu"], va_degree=df.at[idx, "va_degree"])

df = pd.read_excel("read_data_excel.xlsx", sheet_name="line", index_col=0)
for idx in df.index:
    pp.create_line_from_parameters(net, *df.loc[idx, :])

df = pd.read_excel("read_data_excel.xlsx", sheet_name="trafo", index_col=0)
for idx in df.index:
    pp.create_transformer(net, hv_bus=df.at[idx, "hv_bus"], lv_bus=df.at[idx, "lv_bus"],
                          std_type=df.at[idx, "std_type"])

pp.runpp(net)
print(net.res_bus)



