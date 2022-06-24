from collections import UserDict
from contact_book.record import Record


class ContactBook(UserDict):
    """
    Class-container for different contact records
    """
    def __init__(self):
        super().__init__()
        self.counter = 0
        self.names = []

    def add(self, rec: Record) -> None:
        """
        Add new record to the own storage
        :param rec: Record
        :return:
        """
        key = rec.name
        self[key] = rec
        self.names.append(key)

    def __str__(self):
        res = 'My contacts: \n'
        if len(self.data) > 0:
            for key in self.data:
                res += f'{key}\n'
        return res

    def delete(self, key: str) -> bool:
        """
        Delete record with specific key from the storage
        :param key: str
        :return: bool
        """
        if self.data.get(key):
            del self.data[key]
            self.names.remove(key)
            return True
        return False
