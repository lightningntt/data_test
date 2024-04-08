import os
import traceback
import snowflake.connector as snow_connect
from snowflake.connector import DictCursor


os.environ["SNOWFLAKE_SCHEMA"]= 'NEWRELIC'

class SnowflakeConnector: 
    
    def __init__(self):
        """"Create the connection to snowflake"""
        
        self.connector = snow_connect.connect(
                user = os.environ["SNOWFLAKE_USER"],
                account=os.environ["SNOWFLAKE_ACCOUNT"],
                role=os.environ["SNOWFLAKE_ROLE"],
                warehouse=os.environ["SNOWFLAKE_WAREHOUSE"],
                database=os.environ["SNOWFLAKE_DATABASE"],
                schema =os.environ["SNOWFLAKE_SCHEMA"],
                region=os.environ["SNOWFLAKE_REGION"],
                password=os.environ["SNOWSQL_PWD"]
                )


    def query(self, query, verbose):           
        """
        Execture snowsql script and return value of execution.
        """
        if verbose:
            print(f"SQL query: {query}")
        try: 
            return self.connector.cursor(DictCursor).execute(query)
        except: 
            traceback.format_exc()
        