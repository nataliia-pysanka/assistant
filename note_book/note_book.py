from collections import UserDict


# from faker import Faker

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


<<<<<<< Updated upstream
commands = {add_note_command: 'add note',
            add_tag_command: 'add tag',
<<<<<<< HEAD
            change_text_command: 'change text',
            show_single_command: 'show note',
            show_all_command: 'show all',
            search_note_command: 'search note',
            delete_note_command: 'delete name',
            back_command: 'main menu'}

=======
            change_text_command:'change text',
            show_single_command:'show note',
            show_all_command:'show all',
            search_note_command:'search note',
            delete_note_command:'delete name',
            back_command:'main menu'}
=======
commands = {add_note_command: ['add note'],
            add_tag_command: ['add tag'],
            change_text_command: ['change text'],
            show_single_command: ['show note'],
            show_all_command: ['show all'],
            search_note_command: ['search note'],
            delete_note_command: ['delete name'],
            back_command: ['main menu']}
inp_vocab = {'add note':'If you use this option, add note heder,optional tag',
            'add tag':'If you use this option, add existing note header and new tag',
            'change text':'If you use this option, add note header and text to replace',
            'show single':'If you use this option, add note header',
            'show all':'If you use this option, no extra args required',
            'search note':'If you use this option, input to search in tags',
            'delete note':'If you use this option, add note header',
            'main menu':'If you use this option, you will be sent to main menu'
            }
def prompt_nicely():
    print('Please enter your command. Available options are:')
    for comand, prompt in inp_vocab.items():
        print("{:^20} {:<100}".format(comand, prompt))
    return input('>>>')
>>>>>>> Stashed changes
>>>>>>> e784107 (Second day commit, menus ready)

def parser(user_input: str):
    for command, input_ in commands.items():
        for elem in input_:
            if user_input.lower().startswith(elem.lower()):
                data = user_input[len(elem):].strip().split(' ')
                return command, data


def note_book_main():
    while True:
<<<<<<< HEAD
        user_input = input(
            'Please enter your command. Avaliable options are:\n'
            '-----> "add note"<----- If you use this option, add note heder, '
            'optional tag \n '
            # !!!!!!!!!!!!!!!!!!!!!! Решить вариант ввода текста в записку
            '-----> "add tag"<----- If you use this option, add existing note header and new tag\n'
            '-----> "change text"<----- If you use this option, add existing note header and a text to replace previous\n'
            # !!!!!!!!!!!!!!!!!!!!!ТЭг - для поиска, хэдер - для точной идентификации, он должен быть уникальным
            '-----> "change_text_command"<----- If you use this option, add note header and text to replace \n'
            '-----> "show_single_command"<----- If you use this option, add note header\n'
            '-----> "show_all_command"<----- If you use this option, no extra args required\n'
            '-----> "search_note_command"<----- If you use this option, input to search in tags\n'
            '-----> "delete_note_command"<----- If you use this option, add note header\n'
            '-----> "main menu"<----- If you use this option, you will be sent to main menu\n')
        command, data = parser(user_input)
=======
<<<<<<< Updated upstream
            user_input = input('Please enter your command. Avaliable options are:\n'
                               '-----> "add note"<----- If you use this option, add note heder, optional tag \n'
                               #!!!!!!!!!!!!!!!!!!!!!! Решить вариант ввода текста в записку
                               '-----> "add tag"<----- If you use this option, add existing note header and new tag\n'
                               '-----> "change text"<----- If you use this option, add existing note header and a text to replace previous\n'
                               #!!!!!!!!!!!!!!!!!!!!!ТЭг - для поиска, хэдер - для точной идентификации, он должен быть уникальным
                               '-----> "change_text_command"<----- If you use this option, add note header and text to replace \n'
                               '-----> "show_single_command"<----- If you use this option, add note header\n'
                               '-----> "show_all_command"<----- If you use this option, no extra args required\n'
                               '-----> "search_note_command"<----- If you use this option, input to search in tags\n'
                               '-----> "delete_note_command"<----- If you use this option, add note header\n'
                               '-----> "main menu"<----- If you use this option, you will be sent to main menu\n')
            command, data = parser(user_input)
            # command - future function call (add_command, find_phone_command.. etc)
            print(command(*data))
            if result is back_command:
            initial_main()
=======
        user_input = prompt_nicely()
        command, data = parser(user_input)
        #note_body_input=input(f'Please enter note content here, note limit = {note_limet} symbols')
>>>>>>> e784107 (Second day commit, menus ready)
        # command - future function call (add_command, find_phone_command.. etc)
        print(command(*data))
        if command is back_command:
            return
<<<<<<< HEAD
=======
>>>>>>> Stashed changes
>>>>>>> e784107 (Second day commit, menus ready)
