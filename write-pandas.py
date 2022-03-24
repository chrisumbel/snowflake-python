#!/usr/bin/env python
import snowflake.connector
import os
import pandas as pd
from snowflake.connector.pandas_tools import write_pandas

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
    
    df = pd.DataFrame([(1, 'Thingy', 12), (2, 'Dingy', 24)], columns=['ID', 'NAME', 'VAL'])
    success, nchunks, nrows, _ = write_pandas(ctx, df, 'TEST')
except:
    print('Error')
finally:
    cs.close()
ctx.close()

