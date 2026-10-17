import os
from abc import ABC, abstractmethod

from mango.v1.data.Wrappers import cancelable_operation, log
from mango.v1.entities.Table import Table


class Rule_database[T](ABC):
    """
    Upper level entity rules in Specification.
    Contains tables and actions with them.
    """

    @abstractmethod
    def find_table_by_predicate(self, predicate) -> Table | None:
        """
        Inner method of finding table in database.
        :param predicate: predicate function for comparison, should take _Table object and return bool value.
        :return: Table object that equals predicate or None in case of error.
        """
        pass

    @abstractmethod
    def find_table_by_name(self, table_name: str) -> Table | None:
        pass

    @cancelable_operation
    @abstractmethod
    def create_table(self, table_name: str) -> None:
        """
        Creates new file, called table in terms of database.
        :return: None
        """
        pass

    @cancelable_operation
    @abstractmethod
    def delete_table(self, table_name: str) -> None:
        pass

    @abstractmethod
    def get_all_tables(self) -> list[Table]:
        pass

    @log
    @abstractmethod
    def __init_database(self):
        """
        Create database and initialize database architecture by creating folders (tables)
        :return:
        """
        pass
