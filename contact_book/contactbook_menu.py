from contact_book.contactbook import ContactBook


def add_command(*args):
    return 'add_command'


def show_all_command(*args):
    return 'show_all_command'


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
                data = user_input[len(elem):].strip().split(' ')
                return command, data


def contact_book_main():
    while True:
        user_input = input(
            'Please enter your command. Avaliable options are:\n'
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
        if command is back_command:
            return
            # initial_main()


if __name__ == '__main__':
    contact_book_main()
