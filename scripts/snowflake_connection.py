from dotenv import load_dotenv
import os
import snowflake.connector

from utils import pprint, execute_sql

FILEPATH = 'commands.sql'

load_dotenv()

conn = snowflake.connector.connect(
            user=os.getenv("SNOWFLAKE_USER"),
            password=os.getenv("SNOWFLAKE_PASSWORD"),
            account=os.getenv("SNOWFLAKE_ACCOUNT"),
            warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
            role=os.getenv("SNOWFLAKE_ROLE"),
            database=os.getenv("SNOWFLAKE_DATABASE"),
            schema=os.getenv("SNOWFLAKE_SCHEMA")
)

cur = conn.cursor()

execute_sql(FILEPATH, cur)

pprint('list @my_stage', cur)
