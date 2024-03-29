import pandas as pd
from io import StringIO
from src.util.extract_snowflake import SnowflakeConnector
from pandas.testing import assert_frame_equal

connection = SnowflakeConnector()

def test_sample_verify_dw_schema():
    #setup
    csvString = """COLUMN_NAME,DATA_TYPE
name,TEXT
date_id,NUMBER
id,NUMBER
last_loaded_at,TIMESTAMP_NTZ
time_id,NUMBER"""

    # Read from CSV String
    csvStringIO = StringIO(csvString)
    expected_df = pd.read_csv(csvStringIO, sep=",")
    
    #when
    query = f"""select "COLUMN_NAME", "DATA_TYPE" 
                from INFORMATION_SCHEMA.columns 
                where TABLE_NAME = 'accounts' and TABLE_SCHEMA = 'NEW_RELIC_DEV' 
                order by 'COLUMN_NAME'; """

    pd_dw_df = pd.DataFrame(connection.query(query, True))

    #then
    assert_frame_equal(pd_dw_df,expected_df)