import os
import traceback
from unittest import expectedFailure
import snowflake.connector as snow_connect
from snowflake.connector import DictCursor
import pandas as pd


import boto3
import json
from botocore.exceptions import ClientError


def _retrieve_secret(secret_id: str) -> dict:
    """
    Retrieve secrets from the Secrets Manager given the arn

    :param secret_id: str, arn of the Secrets
    :return: json of the Secrets
    """
    try:
        session = boto3.session.Session()
        region_name = session.region_name

        client = session.client(
            service_name='secretsmanager',
            region_name=region_name
        )

        credentials = client.get_secret_value(SecretId=secret_id)

        if 'SecretString' in credentials:
            credentials = credentials['SecretString']

        credentials = json.loads(credentials)

        return credentials

    except Exception as e:
        raise e
        
NEW_RELIC_CREDENTIALS_SECRET = _retrieve_secret("new-relic-credentials")
SNOWFLAKE_CREDENTIALS_SECRET  = _retrieve_secret("snowflake-credential")

os.environ["NEW_RELIC_TOKEN"]     = NEW_RELIC_CREDENTIALS_SECRET["token"]
os.environ["SNOWFLAKE_USER"]      = SNOWFLAKE_CREDENTIALS_SECRET["user_account"]
os.environ["SNOWSQL_PWD"]         = SNOWFLAKE_CREDENTIALS_SECRET["password"]
os.environ["SNOWFLAKE_ACCOUNT"] = SNOWFLAKE_CREDENTIALS_SECRET["account"]
os.environ["SNOWFLAKE_ROLE"] = SNOWFLAKE_CREDENTIALS_SECRET["role"]
os.environ["SNOWFLAKE_WAREHOUSE"] = SNOWFLAKE_CREDENTIALS_SECRET["warehouse"]
os.environ["SNOWFLAKE_DATABASE"] = SNOWFLAKE_CREDENTIALS_SECRET["database"]
os.environ["SNOWFLAKE_REGION"] = SNOWFLAKE_CREDENTIALS_SECRET["region"]
os.environ["SNOWFLAKE_AUTHENTICATOR"] = SNOWFLAKE_CREDENTIALS_SECRET["authenticator"]


class SnowflakeConnector: 
    
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
        