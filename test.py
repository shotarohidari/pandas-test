import pandas as pd
from pandas.testing import assert_frame_equal
from unittest import TestCase

class PandasTestExample(TestCase):
    def test_sample_method(self):
        expected_df = pd.read_csv("test.csv")
        actual_df = pd.read_csv("result.csv")
        assert_frame_equal(actual_df, expected_df)
    
    def test_change_val(self):
        df1 = pd.read_csv("test3.csv")
        df1.iat[0, 7] = 3000
        actual_df = pd.read_csv("test4.csv")
        assert_frame_equal(df1, actual_df)

    # 複数値の変更
    def test_change_val_columns(self):
       df1 = pd.read_csv("test.csv")
       df1.iloc[::, 0] = "○○商事医療法人"
       actual_df = pd.read_csv("result2.csv")
       assert_frame_equal(df1, actual_df)

    # 列をヘッダーで指定した場合の変更
    def test_change_val_columns(self):
       df1 = pd.read_csv("test.csv")
       df1.loc[::, "メーカー型番"] = "NAN"
       actual_df = pd.read_csv("result3.csv")
       assert_frame_equal(df1, actual_df)

    # 1000超える値を999に変更
    def test_cahnge_max_val(self):
        df1 = pd.read_csv("test.csv")
        df1.loc[df1["金額"] > 999, "金額"] = 999
        actual_df = pd.read_csv("result4.csv")
        assert_frame_equal(df1, actual_df)


