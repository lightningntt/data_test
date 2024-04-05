import pandas as pd
from io import StringIO
from src.util.extract_snowflake import SnowflakeConnector
from pandas.testing import assert_frame_equal

connection = SnowflakeConnector()

def test_sample_verify_dw_schema():
    #setup
    csvString = """COLUMN_NAME,DATA_TYPE
name,TEXT
data_checksum,NUMBER
id,NUMBER
data_recorded_at,TIMESTAMP_NTZ
"""

    # Read from CSV String
    csvStringIO = StringIO(csvString)
    expected_df = pd.read_csv(csvStringIO, sep=",")
    
    #when
    query = f"""select "COLUMN_NAME", "DATA_TYPE" 
                from INFORMATION_SCHEMA.columns 
                where TABLE_NAME = 'accounts' and TABLE_SCHEMA = 'NEWRELIC' 
                order by 'COLUMN_NAME'; """

    pd_dw_df = pd.DataFrame(connection.query(query, True))

    #then
    assert_frame_equal(pd_dw_df,expected_df)