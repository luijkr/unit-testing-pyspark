from pyspark.sql import SparkSession, DataFrame
from src.data_transformer import DataTransformer


class TestDataTransformer:
    def test_transform_to_year_month(self, spark: SparkSession, sample_data: DataFrame):
        """
        Tests whether the `year` and `month` columns are created.
        """
        transformer = DataTransformer(spark)
        transformed_df = transformer.transform_to_year_month(sample_data)

        assert transformed_df.count() == 2
        assert "year" in transformed_df.columns
        assert "month" in transformed_df.columns
        assert transformed_df.select("year").distinct().collect() == [(2023,)]
        assert transformed_df.select("month").distinct().collect() == [(10,), (9,)]
