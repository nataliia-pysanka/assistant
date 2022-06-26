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


def days_to_birthday(*args):
    return 'days_to_birthday'


def find_phone_command(*args):
    return 'find_phone_command'


def change_phone_command(*args):
    return 'change_phone_command'


def back_command(*args):
    return 'back_command'


def change_birthday_command(*args):
    return 'change_birthday_command'


def change_name_command(*args):
    return 'change_name_command'


def change_email_command(*args):
    return 'change_email_command'


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


def parser(user_input: str):
    for command, input_ in commands.items():
        for elem in input_:
            if user_input.lower().startswith(elem.lower()):
                data = user_input.strip().split(' ')[1:]
                return command, data


def contact_book_main():
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


if __name__ == '__main__':
    contact_book_main()
