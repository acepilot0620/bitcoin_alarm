import pandas
from pytrends.request import TrendReq

def get_trend(keyword):
    trend_obj = TrendReq()
    trend_obj.build_payload(kw_list=[keyword],timeframe='now 7-d')
    trend_df = trend_obj.interest_over_time()
    trend_list = trend_df.values.tolist()
    return trend_list
