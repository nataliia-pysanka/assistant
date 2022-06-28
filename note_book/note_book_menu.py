from note_book.note_book import Note, NoteBook, Text, Tag, Name
from pathlib import Path

FILE_NOTE_BOOK = 'notebook.json'


class Session:
    def __init__(self, file, book: NoteBook):
        self.file = Path(file)
        self.book = book

    def __enter__(self):
        if self.file.exists():
            pass
            # self.book.load(str(self.file))

    def __exit__(self, exception_type, exception_value, traceback):
        pass
        # self.book.save(str(self.file))


def add_note_command(*args):
    book = args[0]
    name = args[1]
    if name == '':
        print('Name is obligatory parameter')
        input('Press Enter to back in menu >')
        return
    if book.search(name):
        print('Note with such name already exist')
        input('Press Enter to back in menu >')
        return
    try:
        name_obj = Name(name)
    except ValueError as err:
        print(err)
        input('Press Enter to back in menu >')
        return

    tags = []
    for arg in args[2:]:
        try:
            tags.append(Tag(arg))
        except ValueError as err:
            print(err)

    text = input(f'Input text (max {Text.max_text_length} symbols) > ')
    try:
        text_obj = Text(text)
    except ValueError as err:
        print(err)
        text_obj = Text(None)

    note = Note(name=name_obj, text=text_obj, tags=tags)
    book.add(note)
    book.display(name)
    input('Press Enter to back in menu >')


def add_tag_command(*args):
    book = args[0]
    name = args[1]
    if name == '':
        print('Name is obligatory parameter')
        input('Press Enter to back in menu >')
        return
    try:
        tag = args[2]
    except IndexError:
        print('No tag to add')
        input('Press Enter to back in menu >')
        return
    try:
        tag_obj = Tag(tag)
    except ValueError as err:
        print(err)
        input('Press Enter to back in menu >')
        return
    book.add_tag(name, tag_obj)
    book.display(name)
    input('Press Enter to back in menu >')


def change_text_command(*args):
    book = args[0]
    name = args[1]
    if name == '':
        print('Name is obligatory parameter')
        input('Press Enter to back in menu >')
        return
    text = input(f'Input text (max {Text.max_text_length} symbols) > ')
    try:
        text_obj = Text(text)
    except ValueError as err:
        print(err)
        return
    book.add_text(name, text_obj)
    book.display(name)
    input('Press Enter to back in menu >')


def show_single_command(*args):
    book = args[0]
    name = args[1]
    if name == '':
        print('Name is obligatory parameter')
        input('Press Enter to back in menu >')
        return
    note = book.search(name)
    if note:
        note.print()
    else:
        print('No note with such name')
    input('Press Enter to back in menu >')


def show_all_command(*args):
    book = args[0]
    if len(book) > 0:
        book.display_all()
    else:
        print('No notes')
    input('Press Enter to back in menu >')


def search_note_command(*args):
    book = args[0]
    tag = args[1]
    if tag is None:
        print('No tag to search')
        input('Press Enter to back in menu >')
        return
    book.search_tag(tag)


def delete_note_command(*args):
    return 'delete_note_command'


def back_command(*args):
    return 'back_command'


commands = {add_note_command: ['add note'],
            add_tag_command: ['add tag'],
            change_text_command: ['change text'],
            show_single_command: ['show note'],
            show_all_command: ['show all'],
            search_note_command: ['search note'],
            delete_note_command: ['delete note'],
            back_command: ['main menu']}

inp_vocab = {'add note':'If you use this option, add note heder,optional tag',
            'add tag':'If you use this option, add existing note header and new tag',
            'change text':'If you use this option, add note header and text to replace',
            'show note':'If you use this option, add note header',
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


def parser(user_input: str):
    for command, input_ in commands.items():
        for elem in input_:
            if user_input.lower().startswith(elem.lower()):
                data = user_input[len(elem):].strip().split(' ')
                return command, data
    if user_input not in commands.items():
        print('You have typed wrong command. Please try again\n')
        return None


def note_book_main():
    note_book = NoteBook()
    with Session(FILE_NOTE_BOOK, note_book) as session:
        while True:
            user_input = prompt_nicely()
            parsered = parser(user_input)
            if not parsered:
                continue
            command, data = parsered
            if command is back_command:
                return
            command(note_book, *data)

