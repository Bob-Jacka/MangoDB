"""
Rules for clusters entities.
Cluster is a high level entity that can contain several decentralized mangodb bases
"""

from abc import ABC, abstractmethod


class Rule_cluster(ABC):
    @abstractmethod
    def create_database(self, database_name: str):
        pass

    @abstractmethod
    def delete_database(self, database_name: str):
        pass

    @abstractmethod
    def show_databases(self):
        pass
