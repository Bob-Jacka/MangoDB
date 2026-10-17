"""
MangoDB cluster entity, contains and responsible for decentralized databases
"""
from mango.v2.Mangodb.entities import Database
from mango.v2.rules.entities.Rule_cluster import Rule_cluster


class Cluster(Rule_cluster):
    databases: dict[str, Database]

    def __init__(self):
        self.databases = dict()

    def create_database(self, database_name: str):
        pass

    def delete_database(self, database_name: str):
        pass

    def show_databases(self):
        pass
