import os
from abc import ABC, abstractmethod
from typing import (
    Optional
)

from specification.v1.data.Wrappers import (
    cancelable_operation,
    log
)
from specification.v1.entities.Record import Record
from specification.v1.exceptions.DatabaseException import DatabaseException


class Table[R](ABC):
    """
    Quant of book database storage.
    """

    def __init__(self, table_name: str):
        self.table_name = table_name
        self.__inner_table: list[Record] = list()
        self.__init_table()

    def get_table_name(self) -> str:
        return self.table_name

    def get_records(self) -> list[Record]:
        """
        Get all records from table.
        :return: List of records
        """
        return self.__inner_table

    @cancelable_operation
    def add_record(self, record: Record) -> None:
        """
        Add record to table.
        :param record: Record object to add
        """
        try:
            self.__inner_table.append(record)
            self.__save_table()
        except Exception as e:
            raise DatabaseException(f'Error adding record: {e}')

    @cancelable_operation
    @abstractmethod
    def update_record(self, params: dict) -> None:
        """
        Update record by name.
        :param params: Dictionary with name and fields to update
        """
        pass

    @cancelable_operation
    @abstractmethod
    def update_record_by_pattern(self, pattern: str, params: dict) -> None:
        """
        Update records matching regex pattern.
        :param pattern: Regex pattern to match record names
        :param params: Fields to update
        """
        pass

    @cancelable_operation
    @abstractmethod
    def delete_record(self, params: dict) -> None:
        """
        Delete record by parameters.
        :param params: Dictionary with record identification
        """
        pass

    @cancelable_operation
    @abstractmethod
    def delete_record_by_id(self, record_id: int) -> None:
        """
        Delete record by ID.
        :param record_id: Record identifier (int)
        """
        pass

    @cancelable_operation
    def delete_all_records(self) -> None:
        """
        Delete all records from table.
        """
        self.__inner_table.clear()
        self.__save_table()

    @log
    @abstractmethod
    def select_records(self, params: Optional[dict] = None) -> list[Record]:
        """
        Select records from table.
        :param params: Optional filter parameters
        :return: List of matching records
        """
        pass

    @log
    @abstractmethod
    def select_by_pattern(self, pattern: str) -> list[Record]:
        """
        Select records matching regex pattern.
        :param pattern: Regex pattern for book name
        :return: List of matching records
        """
        pass

    @log
    def count_records(self) -> int:
        """
        Count records in table.
        :return: Number of records
        """
        return len(self.__inner_table)

    @log
    @abstractmethod
    def find_record_by_name(self, name: str) -> Optional[Record]:
        """
        Find record by book name.
        :param name: Book name to search
        :return: Record or None
        """
        pass

    @log
    @abstractmethod
    def find_record_by_id(self, record_id: int) -> Optional[Record]:
        """
        Find record by ID.
        :param record_id: Record identifier
        :return: Record or None
        """
        pass

    def __init_table(self) -> None:
        """
        Initialize table file.
        """
        if not os.path.exists(self.table_name):
            with open(self.table_name, 'w+', encoding='utf-8'):
                pass
        else:
            print('Table already exists')

    @abstractmethod
    def __save_table(self) -> None:
        """
        Save table to file.
        """
        try:
            with open(self.table_name, 'w', encoding='utf-8') as f:
                for record in self.__inner_table:
                    line = f'{record.id}|{record.book_name}|{record.book_category}|{record.read_date}|{record.type}\n'
                    f.write(line)
        except Exception as e:
            raise DatabaseException(f'Error saving table: {e}')

    def load_table(self) -> None:
        """
        Load table from file.
        """
        if not os.path.exists(self.table_name):
            return

        try:
            with open(self.table_name, 'r', encoding='utf-8') as f:
                for line in f:
                    parts = line.strip().split('|')
                    if len(parts) >= 5:
                        record = R()
                        self.__inner_table.append(record)
        except Exception as e:
            raise DatabaseException(f'Error loading table: "{e}"')

    def __str__(self) -> str:
        return f'Table(name={self.table_name}, records={self.__inner_table})'

    def __repr__(self) -> str:
        return self.__str__()
