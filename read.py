#!/usr/bin/env python
import snowflake.connector
import os

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
    
    for ticker, close in cs.execute("select Ticker, Close from stock_days;"):
        print("Ticker: {}, Close: {}".format(ticker, close))
except:
    print('Error')
finally:
    cs.close()
ctx.close()

