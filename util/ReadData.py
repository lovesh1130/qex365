import pandas as pd
from sqlalchemy import create_engine


def read_datas():
    engine = create_engine('mysql+pymysql://root:Quant123@35.162.98.89:3306/quantcoin?charset=utf8MB4')
    # table = 'btc_kline_60min'
    sql = '''
        select * from quantcoin.btc_kline_60min;
        '''
    df = pd.read_sql_query(sql, engine)
    return df


if __name__ == '__main__':
    print(read_datas())
