import pytest
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType


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
            StructField("pickup_datetime", StringType(), True),
            StructField("passenger_count", IntegerType(), True),
        ]
    )
    data = [("2023-10-08 12:34:56", 3), ("2023-09-15 08:22:10", 1)]

    return spark.createDataFrame(data, schema=schema)
