from collections import UserDict


def add_note_command():
    return add_note_command


def add_tag_command():
    return add_tag_command


def change_text_command():
    return change_text_command


def show_single_command():
    return show_single_command


def show_all_command():
    return show_all_command


def search_note_command():
    return search_note_command


def delete_note_command():
    return delete_note_command


def back_command():
    return back_command


commands = {add_note_command: ['add note'],
            add_tag_command: ['add tag'],
            change_text_command: ['change text'],
            show_single_command: ['show note'],
            show_all_command: ['show all'],
            search_note_command: ['search note'],
            delete_note_command: ['delete name'],
            back_command: ['main menu']}
inp_vocab = {'add note': 'If you use this option, add note heder,optional tag',
             'add tag': 'If you use this option, add existing note header and new tag',
             'change text': 'If you use this option, add note header and text to replace',
             'show single': 'If you use this option, add note header',
             'show all': 'If you use this option, no extra args required',
             'search note': 'If you use this option, input to search in tags',
             'delete note': 'If you use this option, add note header',
             'main menu': 'If you use this option, you will be sent to main menu'
             }


def prompt_nicely():
    print('Please enter your command. Available options are:')
    for comand, prompt in inp_vocab.items():
        print("{:^20} {:<100}".format(comand, prompt))
    return input('>>>')


def parser(user_input: str):
    for command, input_ in commands.items():
        for elem in input_:
            if user_input.lower().startswith(elem.lower()):
                data = user_input[len(elem):].strip().split(' ')
                return command, data


def note_book_main():
    while True:
        user_input = prompt_nicely()
        command, data = parser(user_input)
        # command - future function call (add_command, find_phone_command.. etc)
        print(command(*data))
        if command is back_command:
            return

if __name__ == '__main__':
    note_book_main()
