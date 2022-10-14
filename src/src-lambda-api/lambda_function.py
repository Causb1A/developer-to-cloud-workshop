import datetime
import boto3
from datetime import date


# Dynamo db client
boto_client = boto3.resource("dynamodb")
dynamo_db_table = boto_client.Table("interconnector-data")


def hour_rounder(t):
    return t.replace(
        second=0, microsecond=0, minute=0, hour=t.hour
    ) + datetime.timedelta(hours=t.minute // 30)


def get_date_keys():
    """Gets the date range of data 2 minutes before current"""
    date_keys = []
    end_range = hour_rounder(datetime.datetime.today())
    start_range = end_range - datetime.timedelta(hours=12)
    while start_range <= datetime.datetime.today():
        start_range += datetime.timedelta(minutes=15)
        date_keys.append(int(start_range.strftime("%Y%m%d%H%M%S")))

    return date_keys


def get_todays_data_from_db():
    """
    Returns the data for today from the database
    """
    todays_date = int(datetime.datetime.today().strftime("%Y%m%d"))
    data = boto_client.batch_get_item(
        RequestItems={
            "interconnector-data": {
                "Keys": [
                    {"datetime": dt, "date": todays_date} for dt in get_date_keys()
                ]
            }
        }
    )

    return data


def lambda_handler(event, context):

    return {"statusCode": 200, "body": get_todays_data_from_db()}
