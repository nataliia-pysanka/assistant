<<<<<<< HEAD
from contact_book.contactbook import ContactBook
from contact_book.record import Record
from pathlib import Path
import pickle

FILE_CONTACT_BOOK = 'contactbook.json'


class Session:
    def __init__(self, file, book: ContactBook):
        self.file = Path(file)
        self.book = book

    def __enter__(self):
        if self.file.exists():
            self.book.load(str(self.file))

    def __exit__(self, exception_type, exception_value, traceback):
        self.book.save(str(self.file))


def add_command(*args):
    book, name = args
    rec = Record(name=name)
    book.add(rec)
    book.display(name)
    input()


def show_all_command(*args):
    book, _ = args
    if len(book) > 0:
        book.display_all()
        input()
=======
from datetime import datetime

from contact_book.contactbook import ContactBook


def add_command(*args):
    return 'add_command'


def show_all_command(*args):
    return 'show_all_command'
>>>>>>> e784107 (Second day commit, menus ready)


def days_to_birthday(*args):
    return 'days_to_birthday'


def find_phone_command(*args):
    return 'find_phone_command'


def change_phone_command(*args):
    return 'change_phone_command'


def back_command(*args):
    return 'back_command'


<<<<<<< HEAD
def change_birthday_command(*args):
    return 'change_birthday_command'
=======
def days_to_birthday(*args):
    if not record.birthday:
        return None
    day_now = datetime.now().date()
    current_year = record.param.replace(year=day_now.year)
    if current_year > day_now:
        delta = current_year - day_now
        print(f'You have left {delta.days} to next birthday!')
        return delta
    else:
        next_b_day = current_year.replace(year=day_now.year + 1)
        delta = next_b_day - day_now
        print(f'You have left {delta.days} to next birthday!')
        return delta
>>>>>>> e784107 (Second day commit, menus ready)


def change_name_command(*args):
    return 'change_name_command'


def change_email_command(*args):
    return 'change_email_command'


<<<<<<< HEAD
commands = {add_command: 'add',
            show_all_command: 'show all',
            days_to_birthday: 'days left',
            find_phone_command: 'find phone',
            change_phone_command: 'change phone',
            back_command: 'main menu',
            # optional section
            change_birthday_command: 'change birthday',
            change_name_command: 'change name',
            change_email_command: 'change email'}
=======
commands = {add_command: ['add'],
            show_all_command: ['show all'],
            # days_to_birthday: ['days left'],
            find_phone_command: ['find phone'],
            change_phone_command: ['change phone'],
            back_command: ['main menu'],
            # optional section
            # change_birthday_command: ['change birthday'],
            change_name_command: ['change name'],
            change_email_command: ['change email']}
inp_vocab_2 = {
    'add': 'If you use this option, add contact name, optional info - phone, birth date, e-mail',
    'show all': 'If you use this option, no extra input required',
    'days left': 'If you use this option, add contact name',
    'find phone': 'If you use this option, add contact name',
    'change phone': 'If you use this option, add cont. name, previous phone number, new phone number',
    'change birthday': 'If you use this option, add contact name,  desired birth date',
    'change name': 'If you use this option, add existing contact name, desired contact name',
    'change email': 'If you use this option, add existing e-mail, desired e-mail',
    'main menu': 'If you use this option, you will be sent to main menu'
}


def prompt_nicely():
    print('Please enter your command. Available options are:')
    for comand, prompt in inp_vocab_2.items():
        print("{:^18} {:<100}".format(comand, prompt))
    return input('>>>')
>>>>>>> e784107 (Second day commit, menus ready)


def parser(user_input: str):
    for command, input_ in commands.items():
        for elem in input_:
            if user_input.lower().startswith(elem.lower()):
<<<<<<< HEAD
                data = user_input.strip().split(' ')[1:]
=======
                data = user_input[len(elem):].strip().split(' ')
>>>>>>> e784107 (Second day commit, menus ready)
                return command, data


def contact_book_main():
<<<<<<< HEAD
    contact_book = ContactBook()
    with Session(FILE_CONTACT_BOOK, contact_book) as session:
        while True:
            user_input = input(
                'Please enter your command. Avaliable options are:\n'
                '-----> "add"<----- If you use this option, add contact '
                'name, optional info - phone, birth date, e-mail\n '
                '-----> "show all"<----- If you use this option, no extra '
                'input required\n '
                '-----> "days left"<----- If you use this option, add contact name\n'
                '-----> "find phone"<----- If you use this option, add contact name\n'
                '-----> "change phone"<----- If you use this option, add contact name, phone number you whant to change --> desired phone number\n'
                '-----> "change birthday"<----- If you use this option, add contact name,  desired birth date\n'
                '-----> "change name"<----- If you use this option, '
                'add existing contact name, desired contact name\n '
                '-----> "change email"<----- If you use this option, add existing e-mail, desired e-mail\n'
                '-----> "main menu"<----- If you use this option, you will be sent to main menu\n')
            command, data = parser(user_input)
            # command - future function call (add_command, find_phone_command.. etc)
            command(contact_book, *data)
            if command is back_command:
                return
=======
    while True:
        user_input = prompt_nicely()
        command, data = parser(user_input)
        # command - future function call (add_command, find_phone_command.. etc)
        print(command(*data))
        if command is back_command:
            return
            # initial_main()
>>>>>>> e784107 (Second day commit, menus ready)


if __name__ == '__main__':
    contact_book_main()
