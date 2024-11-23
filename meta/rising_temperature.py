import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    df=weather.sort_values('recordDate')
    diff=df['temperature'].diff()>0
    dd=df['recordDate'].diff().dt.days==1
    result=weather[diff&dd][['id']]
    return result