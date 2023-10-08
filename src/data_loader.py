from pyspark.sql import SparkSession, DataFrame


class DataLoader:
    def __init__(self, spark) -> None:
        self.spark = spark

    def load(self, filepath: str) -> DataFrame:
        """
        Load the NYC taxi dataset from the given file path.

        Parameters:
            filepath (str): Path to the dataset file.

        Returns:
            DataFrame: Loaded DataFrame containing the NYC taxi data.
        """
        df: DataFrame = (
            self.spark.read.format("csv")
            .option("header", True)
            .option("delimiter", ",")
            .load(filepath)
        )

        return df
