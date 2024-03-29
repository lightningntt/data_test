import os
import traceback
from unittest import expectedFailure
import snowflake.connector as snow_connect
from snowflake.connector import DictCursor
import pandas as pd

class SnowflakeConnector: 
    os.environ["SNOWFLAKE_ACCOUNT"] = "cai.us-east-1"
    os.environ["SNOWFLAKE_ROLE"] = "SNOWFLAKE_CA_ENGINEERING_OPS_CREATORS"
    os.environ["SNOWFLAKE_WAREHOUSE"] = "WHS_ENGINEERING_OPS"
    os.environ["SNOWFLAKE_DATABASE"] = "ENGINEERING_OPERATIONS"
    os.environ["SNOWFLAKE_REGION"] = "us-east-1"
    os.environ["SNOWFLAKE_AUTHENTICATOR"] = "https://coxauto.okta.com"


    def __init__(self):
        """"Create the connection to snowflake"""
        #self.connector = None
        # while True:
            # try:
        self.connector = snow_connect.connect(
                user = os.environ["SNOWFLAKE_USER"],
                account=os.environ["SNOWFLAKE_ACCOUNT"],
                role=os.environ["SNOWFLAKE_ROLE"],
                warehouse=os.environ["SNOWFLAKE_WAREHOUSE"],
                database=os.environ["SNOWFLAKE_DATABASE"],
                schema =os.environ["SNOWFLAKE_SCHEMA"],
                region=os.environ["SNOWFLAKE_REGION"],
                password=os.environ["SNOWSQL_PWD"],
                authenticator=os.environ["SNOWFLAKE_AUTHENTICATOR"]
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
        