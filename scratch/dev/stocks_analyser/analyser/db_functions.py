import pandas as pd

class db_methods:
    # Class variable

    # Initializer / Constructor
    def __init__(self):
        pass

    # Instance method
    def read_db_table(self,table_name=str):
        """
            Pandas methods to collect database table and return a dataframe
            table_name=str|Django Model name
        """
        table_data=table_name.objects.all.values()
        table_dataframe=pd.DataFrame(table_data)
        return table_dataframe

    def read_db_table_with_query(self,table_name=str,query_column_name=str,query_column_value=str):
        """
            Pandas methods to collect database table and return a dataframe
            table_name=str|Django Model name
        """
        table_data=table_name.objects.filter(query_column_name=query_column_value).values()
        table_dataframe=pd.DataFrame(table_data)
        return table_dataframe
