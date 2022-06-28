from multiprocessing.sharedctypes import Value
from pyparsing import nums
from contact_book.contactbook import ContactBook
from contact_book.record import Record, Name, Phone, Email, Birthday
from pathlib import Path
from datetime import datetime

FILE_CONTACT_BOOK = 'contactbook.json'


class Session:
    def __init__(self, file, book: ContactBook):
        self.file = Path(file)
        self.book = book

    def __enter__(self):
        if self.file.exists():
            pass
            # self.book.load(str(self.file))

    def __exit__(self, exception_type, exception_value, traceback):
        pass
        # self.book.save(str(self.file))


def add_command(*args):
    book = args[0]
    name = args[1]
    if name == '':
        print('Name is obligatory parameter')
        input('Press Enter to back in menu >')
        return

    try:
        nums = None if args[2] == '-' else args[2]
    except IndexError:
        nums = None
    try:
        birthday = '' if args[3] == '-' else args[3]
    except IndexError:
        birthday = ''
    try:
        emails = None if args[4] == '-' else args[4]
    except IndexError:
        emails = None

    rec = Record(name=Name(name), num=Phone(nums),
                 birthday=Birthday(birthday), email=Email(emails))

    book.add(rec)
    book.display(name)
    input('Press Enter to back in menu >')


def show_all_command(*args):
    book, _ = args
    if len(book) > 0:
        book.display_all()
        input('Press Enter to back in menu >')


def days_to_birthday(*args):
    book, name = args
    try:
        delta = book.days_to_birthday(name)
        if delta:
            print(delta)
        else:
            print('No information')
        input('Press Enter to back in menu >')
    except ValueError as err:
        print(err)


def find_phone_command(*args):
    book, name = args
    try:
        record = book.search(name)
        if record:
            record.print()
        else:
            print('No information')
        input('Press Enter to back in menu >')
    except ValueError as err:
        print(err)


def change_phone_command(*args):
    book = args[0]
    name = args[1]
    try:
        old_num = args[2]
    except IndexError:
        print('You need to put old number')
        input('Press Enter to back in menu >')

    try:
        new_num = args[3]
    except IndexError:
        print('You need to put new number')
        input('Press Enter to back in menu >')

    try:
        record = book.edit_phone(name, old_num, new_num)
        if record:
            record.print()
        else:
            print('No information')
        input('Press Enter to back in menu >')
    except ValueError as err:
        print(err)


def back_command(*args):
    return 'back_command'


def change_birthday_command(*args):
    book = args[0]
    name = args[1]
    try:
        new_birthday = args[2]
    except IndexError:
        print('You need to put new birthday date')
        input('Press Enter to back in menu >')
        return
    try:
        new_birthday = Birthday(new_birthday)
    except ValueError as err:
        print(err)
        input('Press Enter to back in menu >')
        return
   
    try:
        book.edit_birthday(name, new_birthday)
        record=book.search(name)
        if record:
            record.print()
        else:
            print('No information')
        input('Press Enter to back in menu >')
    except ValueError as err:
        print(err)


def change_name_command(*args):
    return 'change_name_command'


def change_email_command(*args):
    book = args[0]
    name = args[1]
    try:
        old_email = args[2]
    except IndexError:
        print('You need to put old email')
        input('Press Enter to back in menu >')

    try:
        new_email = args[3]
    except IndexError:
        print('You need to put new email')
        input('Press Enter to back in menu >')

    try:
        record = book.edit_email(name, old_email, new_email)
        if record:
            record.print()
        else:
            print('No information')
        input('Press Enter to back in menu >')
    except ValueError as err:
        print(err)


commands = {add_command: ['add'],
            show_all_command: ['show all'],
            days_to_birthday: ['days left'],
            find_phone_command: ['find phone'],
            change_phone_command: ['change phone'],
            back_command: ['main menu'],
            # optional section
            change_birthday_command: ['change birthday'],
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
    print('Please enter your command. Available options are:\n')
    for comand, prompt in inp_vocab_2.items():
        if comand:
            print("{:^18} {:<100}".format(comand, prompt))
    return input('>>>')


def parser(user_input: str):
    for command, input_ in commands.items():
        for elem in input_:
            if user_input.lower().startswith(elem.lower()):
                data = user_input[len(elem):].strip().split(' ')
                return command, data
    if user_input not in commands.items():
        print('You have typed wrong command. Please try again\n')
        contact_book_main()


def contact_book_main():
    contact_book = ContactBook()
    with Session(FILE_CONTACT_BOOK, contact_book) as session:
        while True:
            user_input = prompt_nicely()
            command, data = parser(user_input)
            print(command(contact_book, *data))
            if command is back_command:
                return


if __name__ == '__main__':
    contact_book_main()
