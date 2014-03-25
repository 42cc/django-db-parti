from dbparti.backends import BasePartitionFilter


"""SQLite backend partition filters for django admin"""
class PartitionFilter(BasePartitionFilter):
    """Common methods for all partition filters"""
    pass


class RangePartitionFilter(PartitionFilter):
    """Range partition filter implementation"""

    def apply(self):
        pass

