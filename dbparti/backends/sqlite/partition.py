
from dbparti.backends import BasePartition


"""
SQLite dummy partition backend.
"""
class Partition(BasePartition):

    def prepare(self):
        pass

    def exists(self):
        return True

    def create(self):
        pass


class RangePartition(Partition):
    pass

