import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    return products[(products['recyclable']=='Y') & (products['low_fats']=='Y')]['product_id'].to_frame()