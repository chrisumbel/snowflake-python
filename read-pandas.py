#!/usr/bin/env python
import snowflake.connector
import os
import pandas as pd

# Gets the version
ctx = snowflake.connector.connect(
    user = os.environ['SNOWFLAKE_USER'],
    password = os.environ['SNOWFLAKE_PASSWORD'],
    account = os.environ['SNOWFLAKE_ACCOUNT'],
    #warehouse = 'COMPUTE_WH',
    database = 'STOCKS',
    schema = 'ETL'
    )
cs = ctx.cursor()
cs.execute('use warehouse COMPUTE_WH;')
try:
    #cs.execute("select current_date;")
    
    cs.execute("select Ticker, Close from stock_days;")

    df = cs.fetch_pandas_all()

    print(df)
except:
    print('Error')
finally:
    cs.close()
ctx.close()

