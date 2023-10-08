from pyspark.sql import SparkSession
from src.data_loader import DataLoader


class TestDataReader:
    def test_load(self, spark: SparkSession):
        data_loader = DataLoader(spark)
        filepath = "tests/data/taxis-subset.csv"
        df = data_loader.load(filepath)

        assert df.count() == 10
