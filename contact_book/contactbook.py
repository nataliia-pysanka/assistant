from collections import UserDict
from contact_book.record import Record
from faker import Faker
from datetime import datetime
from random import randint


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
        return None

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

    def __iter__(self):
        return self

    def __next__(self):
        while self.counter < len(self.names):
            if self.counter > 0 and self.counter % 3 == 0:
                input()
            index = self.counter
            self.counter += 1
            return self.data[self.names[index]]

        self.counter = 0
        raise StopIteration

    def search(self, name: str) -> Record:
        """
        Search record in storage by name
        :param name: str
        :return: Record
        """
        if name in self.names:
            rec = self.data.get(name)
            print(rec)
        else:
            print(f'No name {name} in contacts')

    def display_all(self):
        """
        Display all  records
        :return: None
        """
        for record in self:
            print(record)


# class Record:
#     """
#     Class for instance Record
#     """
#
#     def __init__(self, name, birthday, phone):
#         self.name = name
#         self.birthday = birthday
#         self.phone = phone
#
#     def __str__(self):
#         rec = '\t {:<8}...{:<15}'.format('........', '...............') + '\n'
#         rec += '\t {:<8} : {:<15}'.format('Name', self.name) + '\n'
#         rec += '\t {:<8} : {:<15}'.format('Birthday', self.birthday) + '\n'
#         rec += '\t {:<8}...{:<15}'.format('........', '...............') + '\n'
#         rec += '\t {:<8} : {:<15}'.format('Number', self.phone) + '\n'
#         rec += '\t {:<8}...{:<15}'.format('........', '...............') + '\n'
#         return rec
#
#
# fake = Faker()
#
#
# def fake_records(book: ContactBook):
#     for i in range(50):
#         name = fake.first_name()
#         date = fake.date_between(start_date='-70y', end_date='-15y')
#         date_birth = datetime.strftime(date, '%Y-%m-%d')
#         phone = str(fake.random_number(digits=randint(10, 15)))
#         rec = Record(name=name, phone=phone, birthday=date_birth)
#         book.add(rec)
#     return book
#
#
# book = fake_records(ContactBook())
# # book.display_all()
# book.search('Brian')