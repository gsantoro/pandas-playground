# %% import
import pandas as pd

# %%
## Test creating a pandas df
df = pd.DataFrame(
    {
        "a": [4, 5, 6],
        "b": [7, 8, 9],
        "c": [10, 11, 12],
    },
    index=[1, 2, 3],
)

# %%
print(df)