from pyspark.sql import SparkSession, DataFrame
from src.data_transformer import add_pickup_date


def test_add_pickup_date(spark: SparkSession, sample_data: DataFrame):
    """
    Tests whether the `tpep_pickup_date` column is created.
    """
    transformed_df = add_pickup_date(sample_data)

    assert transformed_df.count() == 2
    assert "tpep_pickup_date" in transformed_df.columns
