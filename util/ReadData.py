import pandas as pd
from sqlalchemy import create_engine


def read_datas(startTime, endTime):
    engine = create_engine('mysql+pymysql://root:Quant123@35.162.98.89:3306/quantcoin?charset=utf8MB4')
    # todo 变量输入表名 table = 'btc_kline_60min'
    sql = '''
        select * from quantcoin.btc_kline_60min
        where %(start)s <= id
        and id <= %(endTime)s
        '''
    df = pd.read_sql_query(sql, params={'start': startTime, 'endTime': endTime}, con=engine, index_col='kline_id')
    return df


if __name__ == '__main__':
    start = 1508990400
    end = 1509004800
    print(read_datas(start, end))
