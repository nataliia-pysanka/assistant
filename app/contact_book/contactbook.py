from collections import UserDict
from app.contact_book.record import Record, Birthday, Name, Email, Phone
import json
from datetime import date


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
        key = rec.name.value
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

    def delete_contact(self, contact: Record):
        """
        Delete specific record from the storage
        :param contact: Record
        :return: None
        """
        if contact.name.value in self.names:
            del self.data[contact.name.value]
            self.names.remove(contact.name.value)


    def edit_birthday(self, name: str, new_birthday: str):
        """
        Validate and edit specific person's birthday
        :param name: str,
        :param new_birthday: str
        """
        rec = self.search(name)
        if not rec:
            return 'No record with this name'
        rec.edit_birthday(new_birthday)

    def edit_name(self, name: str, new_name: str):
        """
        Validate and edit specific person's name
        :param name: str, new_name: str
        """
        rec = self.search(name)
        if not rec:
            return 'No record with this name'
        rec.edit_name(new_name)

    def __iter__(self):
        return self

    def __next__(self):
        while self.counter < len(self.names):
            if self.counter > 0 and self.counter % 3 == 0:
                input('Press Enter to continue >')
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

    def search_partly(self, name: str):
        """
        Search record in storage by part of name
        :param name: str
        :return: List[Record]
        """
        contacts = ContactBook()
        for item in self.names:
            if item.lower().startswith(name.lower()):
                contacts.add(self.data.get(item))
        return contacts

    def display(self, name):
        """
        Display specific records
        :return: None
        """
        rec = self.search(name)
        if rec:
            rec.print()
        else:
            print(f'There is no records for name {name}')

    def display_all(self):
        """
        Display all  records
        :return: None
        """
        for record in self:
            record.print()

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
            try:
                dump = json.load(file)
            except ValueError:
                return
        for record in dump:
            rec = Record(name=Name('temp'))
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

    def days_to_birthday(self, name: str):
        """
        Count number of days till specific person's Birthday
        :param name: str
        """
        rec = self.search(name)
        if not rec:
            return 'No record with this name'
        if rec.birthday:
            delta = rec.birthday.days_to_birthday()
            return delta

    def edit_phone(self, name: str, old_num: str, new_num: str):
        """
        Change specific phone number
        :param name: str,
        :param old_num: str,
        :param new_num: str
        """
        rec = self.search(name)
        if not rec:
            return 'No record with this name'
        old_num_obj = rec.get_phone(old_num)
        if old_num_obj:
            old_num_obj.value = new_num
            return rec

    def edit_email(self, name: str, old_email: str, new_email: str):
        """
        Change specific phone number
        :param name: str,
        :param old_email: str,
        :param new_email: str
        """
        rec = self.search(name)
        if not rec:
            return 'No record with this name'
        rec.edit_email(Email(old_email), Email(new_email))
        return rec

    def search_birthday(self, date_format: date):
        """
        Search date in storage by email
        :param date_format: date
        :return: ContactBook
        """
        cb = ContactBook()
        for record in self.data.values():
            if record.birthday is None:
                continue
            if date_format.month == record.birthday.value.month and \
                    date_format.day == record.birthday.value.day:
                cb.add(record)

        if cb:
            return cb
        return None


