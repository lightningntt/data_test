import os
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