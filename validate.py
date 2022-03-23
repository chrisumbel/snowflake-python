#!/usr/bin/env python
import snowflake.connector
import os

# Gets the version
ctx = snowflake.connector.connect(
    user = os.environ['SNOWFLAKE_USER'],
    password = os.environ['SNOWFLAKE_PASSWORD'],
    account = os.environ['SNOWFLAKE_ACCOUNT']
    )
cs = ctx.cursor()
try:
    cs.execute("SELECT current_version()")
    one_row = cs.fetchone()
    print(one_row[0])
except:
    print('Error')
finally:
    cs.close()
ctx.close()

