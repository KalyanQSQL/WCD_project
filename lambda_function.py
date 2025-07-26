import boto3
import os
import json
import toml
import requests
import csv
import snowflake.connector as sf
from dotenv import load_dotenv

s3 = boto3.client("s3")


#def load_config(path="config.toml"):
    #with open(path, "r") as config_file: #I dont think i need this section? i dont have a toml file. 
      #  config = toml.load(config_file)
    #return config


def download_csv(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    return None


def read_csv(file_path):
    with open(file_path, "r", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)


def load_inventory(cursor, schema, my_file_format, local_file_path, file_name, stage_name, table):
    try:
        cursor.execute(f"USE SCHEMA {schema};")

        cursor.execute(
            f"""
            CREATE OR REPLACE FILE FORMAT {my_file_format}
            TYPE = 'CSV'
            FIELD_DELIMITER = ','
            SKIP_HEADER = 1;
            """
        )

        cursor.execute(f"CREATE OR REPLACE STAGE {stage_name} FILE_FORMAT = {my_file_format};")
        cursor.execute(f"PUT file://{local_file_path} @{stage_name} OVERWRITE = TRUE;")
        cursor.execute(f"LIST @{stage_name};")
        cursor.execute(f"TRUNCATE TABLE {schema}.{table};")

        cursor.execute(
            f"""
            COPY INTO {schema}.{table}
            FROM @{stage_name}/{file_name}
            FILE_FORMAT = (FORMAT_NAME = {my_file_format})
            ON_ERROR = 'continue';
            """
        )
    except Exception as e:
        print(f"Error loading inventory: {e}")


def lambda_handler(event, context):
    load_dotenv()

    username = os.getenv("SNOWFLAKE_USERNAME")
    password = os.getenv("SNOWFLAKE_PASSWORD")
    account = os.getenv("SNOWFLAKE_ACCOUNT")
    warehouse = os.getenv("SNOWFLAKE_WAREHOUSE")
    database = os.getenv("SNOWFLAKE_DATABASE")
    schema = os.getenv("SNOWFLAKE_SCHEMA")
    table = os.getenv("SNOWFLAKE_TABLE")
    role = os.getenv("SNOWFLAKE_ROLE")
    stage_name = os.getenv("SNOWFLAKE_STAGE_NAME")
    s3url = os.getenv("S3_URL")
    file_format = os.getenv("SNOWFLAKE_FILE_FORMAT")
    local_file_path = "/tmp/inventory.csv"
    file_name = "inventory.csv"

    content = download_csv(s3url)
    if not content:
        print("Failed to download CSV from S3.")
        return {
            "statusCode": 500,
            "body": "Failed to download CSV from S3.",
        }

    with open(local_file_path, "wb") as temp_file:
        temp_file.write(content)

    read_csv(local_file_path)

    try:
        connection = sf.connect(
            user=username,
            password=password,
            account=account,
            warehouse=warehouse,
            database=database,
            schema=schema,
            role=role,
        )
    except Exception as e:
        print(f"Snowflake connection failed: {e}")
        return {
            "statusCode": 500,
            "body": json.dumps("Connection failed"),
        }

    try:
        cursor = connection.cursor()
        load_inventory(
            cursor,
            schema,
            file_format,
            local_file_path,
            file_name,
            stage_name,
            table,
        )
        print("CSV data uploaded to Snowflake.")
    finally:
        cursor.close()
        connection.close()

    return {
        "statusCode": 200,
        "body": json.dumps("Data Ingestion Completed!!!!!!!!!!!!"),
    }
