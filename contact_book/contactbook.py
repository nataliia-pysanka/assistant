from collections import UserDict
from contact_book.record import Birthday, Record

import json
#from faker import Faker
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
        return ''

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
            return rec

    def display(self, name):
        """
        Display specific records
        :return: None
        """
        rec = self.search(name)
        if rec:
            print(rec)

    def display_all(self):
        """
        Display all  records
        :return: None
        """
        for record in self:
            print(record)

    def edit_birthday(self, name:str, new_birthday:Birthday):
        rec = self.search(name)
        if not rec:
            return 'No record with this name'
        else:
            rec.edit_birthday(new_birthday)
            #return rec

    def __len__(self):
        return len(self.data)

    def save(self, file_name: str):
        """
        Save data in JSON
        :param file_name: str
        """
        dump = []
        for key, record in self.data.items():
            dump.append(record.serealize())
        with open(file_name, 'w', encoding='UTF-8') as file:
            json.dump(dump, file)

    def load(self, file_name: str):
        """
        Load data from JSON to ContactBook object
        :param file_name: str
        """
        self.clear()
        with open(file_name, 'r', encoding='UTF-8') as file:
            dump = json.load(file)
        for record in dump:
            rec = Record()
            rec.deserealize(record)
            self.add(rec)

    def clear(self):
        """
        Clear all the data in the ContactBook
        :return:
        """
        self.counter = 0
        self.names = []
        self.data = {}


# def fake_records(book: ContactBook):
#     for i in range(50):
#         name = fake.first_name()
#         date = fake.date_between(start_date='-70y', end_date='-15y')
#         date_birth = datetime.strftime(date, '%Y-%m-%d')
#         phone = str(fake.random_number(digits=randint(10, 15)))
#         rec = Record(name=name, num=phone, birthday=date_birth)
#         book.add(rec)
#     return book


# if __name__ == '__main__':
#     fake = Faker()
#
#     book = fake_records(ContactBook())
#     # book.display_all()
#     book.save('contactbook.json')
