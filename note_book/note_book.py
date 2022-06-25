from collections import UserDict
import pickle
from pathlib import Path
from contact_book.contactbook import ContactBook

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
    def __str__(self) -> str:
        return self.value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class Text(Field):
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str) -> None:
        if value:
            self.__value = value
        print('Empty note')

    def __str__(self) -> str:
        return self.value

class Name(Field):
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str) -> None:
        if value:
            self.__value = value

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
        self.filename = Path(filename)
        if self.filename.exists():
            with open(self.filename, 'rb') as db:
                self.data = pickle.load(db)

    def add(self, note = Note):
        self.data[note.name.value] = note

    def search(self, tag: str) -> None:
        if tag in self.tag:
            res = self.data.get(tag)
            print(res)
        else:
            print(f'Tag {tag} not found')

    def delete(self, note: Note):
        self.data[note.name.value]

    def __str__(self):
        res = 'My notes: \n'
        if len(self.data) > 0:
            for key in self.data:
                res += f'{key}\n'
            return res
        print ('NoteBook is empty')

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


commands = {add_note_command: 'add note',
            add_tag_command: 'add tag',
            change_text_command: 'change text',
            show_single_command: 'show note',
            show_all_command: 'show all',
            search_note_command: 'search note',
            delete_note_command: 'delete name',
            back_command: 'main menu'}


def parser(user_input: str):
    for command, input_ in commands.items():
        for elem in input_:
            if user_input.lower().startswith(elem.lower()):
                data = user_input[len(elem):].strip().split(' ')
                return command, data


def note_book_main():
    while True:
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
        # command - future function call (add_command, find_phone_command.. etc)
        print(command(*data))
        if command is back_command:
            return
