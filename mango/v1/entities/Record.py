from abc import ABC, abstractmethod


class Record(ABC):
    """
    Quant of database storage table.
    Record consists of user defined types
    """

    def __init__(self):
        pass

    def __str__(self) -> str:
        pass
