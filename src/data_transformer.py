from pyspark.sql import DataFrame
from pyspark.sql.functions import col, to_date


def add_pickup_date(df: DataFrame) -> DataFrame:
    """
    Transform the DataFrame to include pickup date, in addition to the timestamp.

    Parameters:
        df (DataFrame): Input DataFrame.

    Returns:
        DataFrame: Transformed DataFrame with additional pickup date.
    """
    transformed_df = df.withColumn(
        "tpep_pickup_date", to_date(col("tpep_pickup_datetime"))
    )

    return transformed_df
