import os
import types
from abc import ABC, abstractmethod

from specification.v1.data.Wrappers import cancelable_operation, log
from specification.v1.entities.Table import Table
from specification.v1.exceptions.DatabaseException import DatabaseException


class Database[T](ABC):
    """
    Upper level entity in Specification.
    Contains tables and actions with them.
    """

    __tables: list[Table]  # container for tables in database

    def __init__(self, database_name: str):
        self.database_name: str = database_name
        self.__tables = list()
        if not os.listdir().__contains__(database_name):
            self.__init_database()
        else:
            pass

    def find_table_by_predicate(self, predicate) -> Table | None:
        """
        Inner method of finding table in database.
        :param predicate: predicate function for comparison, should take _Table object and return bool value.
        :return: Table object that equals predicate or None in case of error.
        """
        table_to_return = None
        if isinstance(predicate, types.FunctionType):
            for table in self.__tables:
                if predicate(table):
                    table_to_return = table
                    break
            return table_to_return
        else:
            raise DatabaseException(f'Given predicate "{predicate}" is not a function')

    def find_table_by_name(self, table_name: str) -> Table | None:
        table_to_return = None
        for table in self.__tables:
            if table.table_name == table_name:
                table_to_return = table
                break
        return table_to_return

    @cancelable_operation
    def create_table(self, table_name: str) -> None:
        """
        Creates new file, called table in terms of database.
        :return: None
        """
        try:
            if isinstance(T, Table):
                new_table = T(table_name)
                self.__tables.append(new_table)
            else:
                raise Exception('Unknown Table type')
        except Exception as e:
            print(f'An exception occurred during creating table: {e}')

    @cancelable_operation
    def delete_table(self, table_name: str) -> None:
        if not len(self.__tables):
            self.__tables.remove(self.find_table_by_predicate(lambda x: x.get_table_name() == table_name))
        else:
            raise DatabaseException(f'Error during deleting table with given name {table_name}')

    def get_all_tables(self) -> list[Table]:
        if not len(self.__tables) == 0:
            return self.__tables
        else:
            raise DatabaseException('Error in get tables')

    @log
    @abstractmethod
    def __init_database(self):
        """
        Create database and initialize database architecture by creating folders (tables)
        :return:
        """
        pass
