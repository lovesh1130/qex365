import pandas as pd
from sqlalchemy import create_engine


engine = create_engine('mysql+pymysql://root:Quant123@35.162.98.89:3306/quantcoin?charset=utf8MB4')
sql = '''
      select * from quantcoin.btc_kline_60min;
      '''
df = pd.read_sql_query(sql, engine)



