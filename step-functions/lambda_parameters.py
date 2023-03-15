import json 

def lambda_handler(event, context):
    parameters = {
        "S3_BUCKET":"aws-analytics-course", 
        "BRONZE_LAYER_NAMESPACE":"bronze/dms/sales", 
        "BRONZE_LAYER_ECOMMERCE_NAMESPACE":"bronze/kinesis",
        "SILVER_LAYER_NAMESPACE":"silver", 
        "JOB_DATE":"2023/01/12/18",
        "TABLES":"{\"store_orders\": \"currency\", \"store_customers\": \"country\", \"products\": \"product_category\"}",
        "JOIN_COLUMNS_DELTA":"{\"store_orders\": \"order_number\", \"store_customers\": \"email\",  \"products\": \"product_id\"}",
        "JOIN_COLUMNS_INCREMENTAL":"{\"store_orders\": \"order_number\", \"store_customers\": \"email\", \"products\": \"product_category\"}",
        "CURRENCY_CONVERSION_URL":"https://api.exchangerate-api.com/v4/latest/usd",
        "ECOMMERCE_LOGS_BUCKET":"aws-analytics-incoming",
        "ECOMMERCE_STREAM_DATE":"2023/01/31/17",
		"GLUE_SILVER_DATABASE":"electroniz_curated",
        "datalake-formats":"delta",
		"job-language":"python-3",
		"TempDir":"s3://aws-analytics-course/temp/", 
		"enable-glue-datacatalog":"true"
        }
    return parameters