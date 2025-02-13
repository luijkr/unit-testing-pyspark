import pytest
from datetime import datetime
from pyspark.sql import SparkSession
from pyspark.sql.types import (
    StructType,
    StructField,
    IntegerType,
    DoubleType,
    TimestampType,
)


@pytest.fixture(scope="session")
def spark():
    """
    Fixture for creating a SparkSession.
    """
    spark = SparkSession.builder.appName("TestApp").master("local[*]").getOrCreate()
    yield spark
    spark.stop()


@pytest.fixture(scope="session")
def sample_data(spark):
    """
    Fixture for creating a sample DataFrame.
    """
    schema = StructType(
        [
            StructField("tpep_pickup_datetime", TimestampType(), True),
            StructField("tpep_dropoff_datetime", TimestampType(), True),
            StructField("trip_distance", DoubleType(), True),
            StructField("fare_amount", DoubleType(), True),
            StructField("pickup_zip", IntegerType(), True),
            StructField("dropoff_zip", IntegerType(), True),
        ]
    )
    data = [
        (
            datetime(2025, 1, 1, 0, 0, 0),
            datetime(2025, 1, 1, 0, 1, 0),
            1.0,
            10.0,
            10001,
            10002,
        ),
        (
            datetime(2025, 1, 2, 0, 0, 0),
            datetime(2025, 1, 2, 0, 1, 0),
            2.0,
            20.0,
            20001,
            20002,
        ),
    ]

    return spark.createDataFrame(data, schema=schema)
