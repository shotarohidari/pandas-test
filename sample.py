import pandas as pd
from pandas.testing import assert_frame_equal
df1 = pd.read_csv("test.csv")
# df1.loc[::, "金額"] = 999
# print(df1["金額"])
df1.loc[df1["金額"] > 999, "金額"] = 999
print(df1)
# print(df1)
# actual_df = pd.read_csv("result3.csv")
# assert_frame_equal(df1, actual_df)
