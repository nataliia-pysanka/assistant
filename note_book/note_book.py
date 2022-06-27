from collections import UserDict
import json
from faker import Faker
from random import randint
from typing import List


class Field:

    def __init__(self, value):
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def __str__(self):
        return f"{self.value}"


class Tag(Field):
    max_tag_length = 10
    allowed_chars = set(
        '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

    @Field.value.setter
    def value(self, value: str) -> None:
        if not set(value).issubset(Tag.allowed_chars):
            print(f"{value} Incorrect characters in tag")
            return
        elif len(value) > Tag.max_tag_length:
            print(f"Tags can be less than {Tag.max_tag_length} characters")
            return
        Field.value.fset(self, value)


class Text(Field):
    max_text_length = 200

    @Field.value.setter
    def value(self, value: str):
        if len(value) > 200:
            print(f"Text can be less than {Text.max_text_length} characters")
            return
        Field.value.fset(self, value)


class Name(Field):
    max_name_length = 15

    @Field.value.setter
    def value(self, new_value: str):
        if len(new_value) > Name.max_name_length:
            print(f"Name should contain under {Name.max_name_length} "
                  f"characters")
            return
        Field.value.fset(self, new_value)


class Note:

    def __init__(self, name: Name, text: Text = None, tags: List[Tag] = None):
        self.name = name
        self.tags = tags
        self.text = text

    def add_tag(self, new_tag: Tag):
        if not isinstance(new_tag, Tag):
            print('\t Tag can not be added \n')
            return
        if new_tag.value not in [t.value for t in self.tags]:
            self.tags.append(new_tag)
            return new_tag

    def add_text(self, new_txt: Text):
        if not isinstance(new_txt, Text):
            print('\t Text can not be added \n')
            return
        if not self.text:
            self.text = new_txt

    def delete_tag(self, tag: Tag):
        if not isinstance(tag, Tag):
            print('\t Number not identified, Phone entered incorrectly \n')
            return
        if tag in self.tags:
            self.tags.remove(tag)
        else:
            print(f'\t The tag {tag} is not found \n')

    def __str__(self):
        rec = '.'*80 + '\n'
        for key, value in self.__dict__.items():
            rec += '{:<8} : {:<15}'.format(key.upper().replace('_', ''),
                                            str(value) if value else '') + '\n'
        rec = '.'*80 + '\n'
        return rec


class NoteBook(UserDict):

    def __init__(self):
        super().__init__()
        self.counter = 0

    def add(self, note: Note):
        key = note.name
        self[key] = note

    def search(self, tag: str):
        for note in self.data.values():
            if tag in note.tag:
                print(note)

    def delete(self, note: Note):
        if note.name in self.data:
            del self.data[note.name]

    def __str__(self):
        res = 'My notes: \n'
        if len(self.data) > 0:
            for key, value in self.data.items():
                res += f'{key}\n'
            return res
        print('NoteBook is empty')

    def display_all(self):
        """
        Display all  records
        :return: None
        """
        for record in self:
            print(record)

    # def save(self, filename: str):
    #
    #     dump = []
    #     for tag, note in self.data.items():
    #         dump.append(note.serealize())
    #     with open(filename, 'w', encoding='UTF-8') as f:
    #         json.dump(dump, f)
    #
    # def load(self, filename: str):
    #
    #     self.clear()
    #     with open(filename, 'r', encoding='UTF-8') as f:
    #         dump = json.load(f)
    #     for note in dump:
    #         txt = Note()
    #         txt.deserealize(note)
    #         self.add(txt)


def fake_records(book: NoteBook):
    for i in range(50):
        name = Name(fake.text(max_nb_chars=Name.max_name_length)[:-1])
        text = Text(fake.text(max_nb_chars=Text.max_text_length)[:-1])
        tags = []
        for _ in range(randint(1, 5)):
            tag = Tag(fake.text(
                max_nb_chars=Tag.max_tag_length)[:-1].replace(' ', ''))
            tags.append(tag)

        note = Note(name=name, text=text, tags=tags)
        print(note)
        book.add(note)
    return book


if __name__ == '__main__':
    fake = Faker()

    book = fake_records(NoteBook())
    book.display_all()
    # book.save('contactbook.json')
