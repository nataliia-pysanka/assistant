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

# to Field class
# @property
#     def param(self):
#         return self._param

class Birthday(Field):
@Field.param.setter
    def param(self, data):
        try:
            self._param = datetime.strptime(data, '%d.%m.%Y').date()
        except:
            raise ValueError("Birthday format issue. Please enter birthday in DD.MM.YY format")
    def days_to_birthday(self):
        if not self.b_day:
            return None
        day_now = datetime.now().date()
        current_year = self.b_day.param.replace(year=day_now.year)
        if current_year > day_now:
            delta = current_year - day_now
            print(f'You have left {delta.days} to next birthday!')
            return delta
        else:
            next_b_day = current_year.replace(year=day_now.year + 1)
            delta = next_b_day - day_now
            print(f'You have left {delta.days} to next birthday!')
            return delta

commands = {add_command:'add',
            show_all_command: 'show all',
            days_to_birthday: 'days left',
            find_phone_command:'find phone',
            change_phone_command:'change phone',
            back_command:'main menu',
            #optional section
            change_birthday_command:'change birthday',
            change_name_command:'change name',
            change_email_command:'change email'}


def parser(user_input: str):
  for command, input_ in commands.items():
    for elem in input_:
      if user_input.lower().startswith(elem.lower()):
        data = user_input[len(elem):].strip().split(' ')
        return command, data

def contact_book_main():
    while True:
            user_input = input('Please enter your command. Avaliable options are:\n'
                               '-----> "add"<----- If you use this option, add contact name, optional info - phone, birth date, e-mail\n'
                               '-----> "show all"<----- If you use this option, no extra input required\n'
                               '-----> "days left"<----- If you use this option, add contact name\n'
                               '-----> "find phone"<----- If you use this option, add contact name\n'
                               '-----> "change phone"<----- If you use this option, add contact name, phone number you whant to change --> desired phone number\n'
                               '-----> "change birthday"<----- If you use this option, add contact name,  desired birth date\n'
                               '-----> "change name"<----- If you use this option, add existing contact name, desired contact name\n'
                               '-----> "change email"<----- If you use this option, add existing e-mail, desired e-mail\n'
                               '-----> "main menu"<----- If you use this option, you will be sent to main menu\n')
            command, data = parser(user_input)
            # command - future function call (add_command, find_phone_command.. etc)
            print(command(*data))
            if result is back_command:
            initial_main()
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
