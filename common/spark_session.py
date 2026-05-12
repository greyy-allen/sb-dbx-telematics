def get_spark():
    try:
        from databricks.connect import DatabricksSession
        from databricks.sdk.core import Config
        config = Config(profile="DEFAULT")
        return DatabricksSession.builder.sdkConfig(config).getOrCreate()
    except ImportError:
        from pyspark.sql import SparkSession
        return SparkSession.builder.getOrCreate()


spark = get_spark()
