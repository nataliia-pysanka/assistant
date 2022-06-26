from collections import UserDict
import json

# from faker import Faker

class Field:

    def __init__(self, value):
        self.__value = value
        self.value = value

    def __str_(self):
        return self.value

    def __repr__(self):
        return self.value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value


class Tag(Field):

    @Field.value.setter
    def value(self, value: str) -> None:
        max_tag_length = 10
        allowed_chars = set('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

        if set(value).issubset(allowed_chars):
            try:
                len(value) < max_tag_length
            except:
                raise AttributeError(f"Tags can only be under {max_tag_length} characters")
        raise ValueError("Value Error, Tags can only contain letters and numbers")

    def __str__(self) -> str:
        return self.value


class Text(Field):

    @property
    def value(self) -> str:
        return self.value

    @value.setter
    def value(self, value: str) -> None:
        if value:
            self.value = value
        print('Empty note')

    def __str__(self) -> str:
        return self.value

class Name(Field):

    @Field.value.setter
    def value(self, value: str) -> None:
        max_name_length = 15

        try:
            len(value) < max_name_length
        except:
            raise AttributeError(f"Name should contain under {max_name_length} characters")
        self._value = value

    def __str__(self) -> str:
        return self.value


class Note:

    def __init__(self, data: str, tag: Tag = None) -> None:
        self.tags = []
        self.data = data
        if tag:
            self.tags.append(tag)

class NoteBook(UserDict):

    def __init__(self, filename: str) -> None:
        super().__init__()
        self.counter = 0

    def add(self, note = Note):
        if isinstance(note, Note):
            if note.field.value in self.data.keys():
                self.data.update({note.name.value: note})
            else:
                self.data[note.name.value] = note

    def search(self, tag: str) -> None:
        if tag in self.tag:
            res = self.data.get(tag)
            print(res)
        else:
            print(f'Tag {tag} not found')

    def delete(self, note: Note):
        if isinstance(note, Note):
            del self.data[note.name.value]

    def __str__(self):
        res = 'My notes: \n'
        if len(self.data) > 0:
            for key in self.data:
                res += f'{key}\n'
            return res
        print ('NoteBook is empty')

    def save(self, filename: str):

        dump = []
        for tag, note in self.data.items():
            dump.append(note.serealize())
        with open(filename, 'w', encoding='UTF-8') as f:
            json.dump(dump, f)

    def load(self, filename: str):

        self.clear()
        with open(filename, 'r', encoding='UTF-8') as f:
            dump = json.load(f)
        for note in dump:
            txt = Note()
            txt.deserealize(note)
            self.add(txt)

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
        print(command(*data))
        if command is back_command:
            return

