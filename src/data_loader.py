from pyspark.sql import SparkSession, DataFrame


def load_taxi_data(
    spark: SparkSession, table_name: str = "samples.nyctaxi.trips"
) -> DataFrame:
    """
    Load the NYC taxi dataset from the `samples` catalog.

    Parameters:
        spark (SparkSession): Spark session object.

    Returns:
        DataFrame: Loaded DataFrame containing the NYC taxi data.
    """
    df: DataFrame = spark.table(table_name)

    return df
