from app.contact_book.contactbook import ContactBook
from app.contact_book.record import Record, Name, Phone, Email, Birthday
from pathlib import Path
import pkg_resources
from datetime import datetime

FILE_CONTACT_BOOK = pkg_resources.resource_filename(__name__,
                                                    'contactbook.json')


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
    """
    Adding data to the record command and parameter validation
    """
    book = args[0]
    name = args[1]
    if name == '':
        print('Name is obligatory parameter')
        input('Press Enter to back in menu >')
        return

    if book.search(name):
        print('This name already in use')
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

    try:
        name_obj = Name(name)
    except ValueError as err:
        print(err)
        return

    num_obj = None
    if nums:
        try:
            num_obj = Phone(nums)
        except ValueError as err:
            print(err)

    birth_obj = None
    if birthday:
        try:
            birth_obj = Birthday(birthday)
        except ValueError as err:
            print(err)

    email_obj = None
    if emails:
        try:
            email_obj = Email(emails)
        except ValueError as err:
            print(err)

    rec = Record(name=name_obj, num=num_obj,
                 birthday=birth_obj, email=email_obj)

    book.add(rec)
    book.display(name)
    input('Press Enter to back in menu >')


def show_all_command(*args):
    """
    Adding data to the record command and parameter validation
    """
    book, _ = args
    if len(book) > 0:
        book.display_all()
    else:
        print('No contacts in contactbook!')
    input('Press Enter to back in menu >')


def days_to_birthday(*args):
    """
    Getting number of days till the specific person's birthday and validation
    """
    book, name = args
    try:
        delta = book.days_to_birthday(name)
        if delta:
            print(delta)
        else:
            print('No information')
    except ValueError as err:
        print(err)
    input('Press Enter to back in menu >')


def find_phone_command(*args):
    """
    Command for getting phone by name and validation
    """
    book, name = args
    try:
        contacts: ContactBook = book.search_partly(name)
        if contacts:
            contacts.display_all()
        else:
            print('No information')
        input('Press Enter to back in menu >')
    except ValueError as err:
        print(err)


def change_phone_command(*args):
    """
    Command for changing phone by name and validation
    """
    book = args[0]
    name = args[1]
    if name == '':
        print('Name is obligatory parameter')
        input('Press Enter to back in menu >')
        return

    record = book.search(name)
    if not record:
        print('No record with such name')
        input('Press Enter to back in menu >')
        return

    try:
        one_num = args[2]
    except IndexError:
        print('You need to put new number')
        input('Press Enter to back in menu >')
        return

    if not record.get_phone(one_num):
        record.add_phone(Phone(one_num))

    try:
        new_num = args[3]
    except IndexError:
        record.print()
        input('Press Enter to back in menu >')
        return

    record = book.edit_phone(name, one_num, new_num)
    if record:
        record.print()
    else:
        print('No information')
    input('Press Enter to back in menu >')


def back_command():
    """
    Exit back to the menu command
    """
    return 'back_command'


def change_birthday_command(*args):
    """
    Change specific person's birth date command
    """ 
    book = args[0]
    name = args[1]
    if name == '':
        print('Name is obligatory parameter')
        input('Press Enter to back in menu >')
        return

    record = book.search(name)
    if not record:
        print('No contact with such name')
        return

    try:
        new_birthday = args[2]
    except IndexError:
        print('You need to put new birthday date')
        input('Press Enter to back in menu >')
        return

    try:
        book.edit_birthday(name, new_birthday)
        record = book.search(name)
        if record:
            record.print()
        else:
            print('No information')
        input('Press Enter to back in menu >')
    except ValueError as err:
        print(err)


def change_name_command(*args):
    """
    Change specific name command
    """
    book = args[0]
    name = args[1]
    try:
        new_name = args[2]
    except IndexError:
        print('You need to put new name')
        input('Press Enter to back in menu >')
        return

    try:
        book.edit_name(name, new_name)
        record = book.search(name)
        if record:
            record.print()
        else:
            print('No information')
        input('Press Enter to back in menu >')
    except ValueError as err:
        print(err)


def change_email_command(*args):
    """
        Change specific email command
    """
    book = args[0]
    name = args[1]
    if name == '':
        print('Name is obligatory parameter')
        input('Press Enter to back in menu >')
        return

    record = book.search(name)
    if not record:
        print('No contact with such name')
        return

    try:
        one_email = args[2]
    except IndexError:
        print('You need to put new number')
        input('Press Enter to back in menu >')
        return
    if not record.get_email(one_email):
        record.add_email(Email(one_email))

    try:
        new_email = args[3]
    except IndexError:
        record.print()
        input('Press Enter to back in menu >')
        return

    record = book.edit_email(name, one_email, new_email)
    if record:
        record.print()
    else:
        print('No information')
    input('Press Enter to back in menu >')


def who_born(*args):
    """
        Search contacts that have birthday in specific day
    """
    book = args[0]
    try:
        date = datetime.strptime(str(args[1]), '%d.%m.%Y').date()
    except ValueError:
        print("Birthday format issue. Please enter birthday "
              "in DD.MM.YY format")
        input('Press Enter to back in menu >')
        return
    contacts = book.search_birthday(date)
    if contacts:
        contacts.display_all()
    else:
        print(f'\t Birthday {date} is not found \n')
    input('Press Enter to back in menu >')


def delete_contact_command(*args):
    """
    Deleting comment by it's name command
    """
    book = args[0]
    name = args[1]
    if name == '':
        print('Name is obligatory parameter')
        input('Press Enter to back in menu >')
        return
    contact = book.search(name)
    if contact:
        book.delete_contact(contact)
        print(f'Record for {name} was eradicated')  # delete method
    else:
        print('No contact with such name')
    input('Press Enter to back in menu >')


commands = {add_command: ['add'],
            show_all_command: ['show all'],
            days_to_birthday: ['days left'],
            who_born: ['who born'],
            find_phone_command: ['find phone'],
            change_phone_command: ['change phone'],
            back_command: ['main menu'],
            # optional section
            change_birthday_command: ['change birthday'],
            change_name_command: ['change name'],
            change_email_command: ['change email'],
            delete_contact_command: ['delete']}

inp_vocab_2 = {
    'add': 'If you use this option, add contact name, optional info - phone, birth date, e-mail',
    'show all': 'If you use this option, no extra input required',
    'days left': 'If you use this option, add contact name',
    'who born': 'If you use this option, add date in DD.MM.YY format',
    'find phone': 'If you use this option, add contact name',
    'change phone': 'If you use this option, add cont. name, previous phone number, new phone number',
    'change birthday': 'If you use this option, add contact name,  desired birth date',
    'change name': 'If you use this option, add existing contact name, desired contact name',
    'change email': 'If you use this option, add existing e-mail, desired e-mail',
    'delete': 'If you use this option, add existing contact name',
    'main menu': 'If you use this option, you will be sent to main menu'
}


def prompt_nicely():
    """
    Options hint for user input
    """
    print('Please enter your command. Available options are:\n')
    for comand, prompt in inp_vocab_2.items():
        if comand:
            print("{:^18} {:<100}".format(comand, prompt))
    return input('>>>')


def parser(user_input: str):
    """
    Searching if the given command is available
    """
    for command, input_ in commands.items():
        for elem in input_:
            if user_input.lower().startswith(elem.lower()):
                data = user_input[len(elem):].strip().split(' ')
                return command, data
    if user_input not in commands.items():
        print('You have typed wrong command. Please try again\n')
        input('Press Enter to back in menu >')
        return None


def contact_book_main():
    """
    Working with current contactbook session
    """
    contact_book = ContactBook()
    with Session(FILE_CONTACT_BOOK, contact_book) as session:
        while True:
            user_input = prompt_nicely()
            parsered = parser(user_input)
            if not parsered:
                continue
            command, data = parsered
            if command is back_command:
                return
            command(contact_book, *data)


if __name__ == '__main__':
    contact_book_main()
