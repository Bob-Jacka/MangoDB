from mango.v1.entities.Table import Table
from mango.v2.rules.entities.Rule_database import Rule_database


class Database(Rule_database):

    def __init__(self):
        pass

    def find_table_by_predicate(self, predicate) -> Table | None:
        pass

    def find_table_by_name(self, table_name: str) -> Table | None:
        pass

    def create_table(self, table_name: str) -> None:
        pass

    def delete_table(self, table_name: str) -> None:
        pass

    def get_all_tables(self) -> list[Table]:
        pass
