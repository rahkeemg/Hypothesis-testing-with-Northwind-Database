import sqlite3
import pandas as pd


class MyConn:

    def __init__(self, filename=None):
        self.__connection(filename=filename)

    def __connection(self, filename):
        """

        :param filename:
            Method to etablish the connection to the database
        :return:
        """
        self._conn = sqlite3.connect(filename)
        self.cursor = self._conn.cursor()
        print('Connection established')

    def close_connection(self):
        """
        Method to close sqlite3 connection
        :return:
        """
        self._conn.close()
        print('-'*50)
        print('--------------- CLOSING CONNECTION ---------------')
        print('-'*50)

    def database_tables(self):
        """
            Method to get all of the SQL Database tables
        :return:
            A list of the tables in the SQL database
        """
        query = """
            SELECT name
            FROM sqlite_master 
            WHERE type = 'table';
        """
        self.cursor.execute(query)
        res = self.cursor.fetchall()
        table_names = [r[0] for r in res]
        return table_names

    @staticmethod
    # Currently not used.  Consider deleting before final submission
    def build_query(query=None):
        # TODO: Possibly add functionality to prevent against SQL injections
        #       If additional functionality is not added to take care of SQL injections,
        #         see about deleting, since this method does not do anything unique
        #       This method is currently not used.  To subsitute this, can just format
        #         the query in question as a string with triple single/double quotes and
        #         pass it into the run query method(s)
        """
            Method to generate an SQL query to run
        :param query:
            The database query to run.  When entering, use triple quotes &
            place the semi-colon appropriately to end the SQL statement.
            Ex:
                '''
                    SELECT *
                    FROM <table_name>;
                '''
        :return:
            The string representation of the query to run in SQL
        """
        return query

    @staticmethod
    def build_select_all_query(table_name=None):
        """
            Static method to build 'SELECT *' query
        :param table_name:
            Table to select information from
        :return:
            Select All query string of the table in question
        """
        res = f'SELECT * FROM {table_name};'
        return res

    def select_all_from_table(self, table_name=None, load_df=False):
        """
            Method to select all info from input table
        :table_name:
            Table name to select information from
        :load_df {bool}:
            Flag to load table information into a data frame
                ~ True: load table information as a dataframe
                ~ False: load table information as a list
        :return:
            The information from the selected table as a list or a dataframe
            depending on the load_df flag
        """
        query = self.build_select_all_query(table_name)
        res = self.cursor.execute(query).fetchall()
        if not load_df:
            return res
        else:
            df = self.load_dataframe(query)
            return df

    def list_table_columns(self, table_name):
        """

        :param table_name:
            Table name to get the columns from in sql
        :return:
            A dictionary with the table information
        """
        query = f'PRAGMA table_info({table_name});'
        res = self.cursor.execute(query).fetchall()
        return res

    def load_dataframe(self, query):
        df = pd.read_sql(query, self._conn)
        return df

    def run_query(self, query, load_df=False):
        """
            Method to run the input query and return the results
        :params 
            query: str
                SQL query to run against the database
                    '''
                        SELECT *
                        FROM <table_name>;
                    '''
            load_df: bool
                Flag wether or not the information returned by the SQL Query should be returned as a dataframe. 
                    ~ True: Return as dataframe
                    ~ False: Return as a list of tuples
        :return
            Query results either in a list of tuples or a dataframe depending on load_df flag.
            If there are no results, an empty list will be returned
        """
        if not load_df:
            res = self.cursor.execute(query).fetchall()
            return res
        else:
            df = self.load_dataframe(query)
            return df
