from contact_book.contactbook import ContactBook
from contact_book.record import Name, Record, Phone
from pathlib import Path

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
    book, name, phone = args
    rec = Record(name=Name(name),num=Phone(phone))
    book.add(rec)
    book.display(name)
    input()

def add_phone_command(*args):
    book, name, phone = args
    rec = book[name]
    rec.add(Phone(phone))
    print(rec)
    book.display(name)
    input()

def show_all_command(*args):
    book, _ = args
    if len(book) > 0:
        book.display_all()
        input()

def show_number_command(*args):
    user = contact_book.get(args[0])
    result = ''
    for phone in user.phones:
        result += phone.value + ' and '
        print(result) #temp

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


commands = {add_phone_command:['add phone'],
            add_command: ['add'],
            show_all_command: ['show all'],
            show_number_command: ['show number'],
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
    'add phone': 'If you use this option, add contact name, new phone number',
    'show all': 'If you use this option, no extra input required',
    'show number': 'If you use this option, add contact name',
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


def parser(user_input: str):
    for command, input_ in commands.items():
        for elem in input_:
            if user_input.lower().startswith(elem.lower()):
                data = user_input[len(elem):].strip().split(' ')
                return command, data


def contact_book_main():
    contact_book = ContactBook()
    with Session(FILE_CONTACT_BOOK, contact_book) as session:
        while True:
            user_input = prompt_nicely()
            command, data = parser(user_input)
            command(contact_book, *data)
            if command is back_command:
                return


if __name__ == '__main__':
    contact_book_main()
