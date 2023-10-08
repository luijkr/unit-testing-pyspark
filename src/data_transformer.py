from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import col, year, month


class DataTransformer:
    def __init__(self, spark: SparkSession):
        self.spark = spark

    def transform_to_year_month(self, df: DataFrame) -> DataFrame:
        """
        Transform the DataFrame to include columns for year and month.

        Parameters:
            df (DataFrame): Input DataFrame.

        Returns:
            DataFrame: Transformed DataFrame with additional year and month columns.
        """
        transformed_df = (
            df
            .withColumn("year", year(col("pickup_datetime")))
            .withColumn("month", month(col("pickup_datetime")))
        )
        return transformed_df
