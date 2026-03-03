# %%
import pandas as pd
df = pd.read_parquet("simulation_events.parquet")
# %%
print(df.shape)
# %%
print(df.dtypes)
# %%
print(df.head(50))