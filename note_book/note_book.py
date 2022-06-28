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
            raise ValueError(f"Incorrect characters in tag")
        elif len(value) > Tag.max_tag_length:
            raise ValueError(f"Tags cant be less than {Tag.max_tag_length} characters")
        # Field.value.fset(self, value)
        self._value = value


class Text(Field):
    max_text_length = 200

    @Field.value.setter
    def value(self, value: str):
        if len(value) > 200:
            raise ValueError(f"Text can't be less than {Text.max_text_length} "
                             f"characters")
        # Field.value.fset(self, value)
        self._value = value


class Name(Field):
    max_name_length = 15

    @Field.value.setter
    def value(self, new_value: str):
        if len(new_value) > Name.max_name_length:
            raise ValueError(f"Name should contain under "
                             f"{Name.max_name_length} characters")
        Field.value.fset(self, new_value)


class Note:

    def __init__(self, name: Name, text: Text = None, tags: List[Tag] = None):
        self.name = name
        self.tags = tags
        self.text = text

    def add_tag(self, new_tag: Tag):
        if not isinstance(new_tag, Tag):
            raise TypeError('\t Tag can not be added \n')
        if new_tag.value not in self.tags:
            self.tags.append(new_tag)
            return new_tag

    def add_text(self, new_txt: Text):
        if not isinstance(new_txt, Text):
            raise TypeError('\t Text can not be added \n')
        if not self.text:
            self.text = new_txt

    def delete_tag(self, tag: Tag):
        if not isinstance(tag, Tag):
            raise TypeError('\t Incorrect type of tag \n')
        if tag in self.tags:
            self.tags.remove(tag)
        else:
            print(f'\t The tag {tag} is not found \n')

    def __str__(self):
        return f'Note: {self.name.value}'

    def print(self):
        rec = '.' * 120 + '\n'

        rec += '\t  {:<8} : {:<15}'.format('NAME', str(self.name.value)) + '\n'

        tags = ' '.join(str(tag.value) for tag in self.tags)
        rec += '\t  {:<8} : {:<15}'.format(f'TAGS', tags + '\n')

        rec += '.' * 120 + '\n'
        rec += '{:^120}'.format(self.text.value)
        rec += '\n'
        rec += '.' * 120 + '\n'
        print(rec)

    def has_tag(self, tag: str):
        for tag_value in self.tags:
            if tag_value.value == tag:
                return True
        return False


class NoteBook(UserDict):

    def __init__(self):
        super().__init__()
        self.counter = 0

    def add(self, note: Note):
        key = note.name.value
        self.data[key] = note
        print(self.data.keys())

    def search_tag(self, tag: str):
        for note in self.data.values():
            if note.has_tag(tag):
                note.print()

    def delete(self, note: Note):
        if note.name in self.data:
            del self.data[note.name]

    def display_all(self):
        """
        Display all  records
        :return: None
        """
        for record in self.data.values():
            record.print()

    def search(self, name: str) -> Note:
        """
        Search note in storage by name
        :param name: str
        :return: Note
        """
        if name in self.data.keys():
            note = self.data.get(name)
            return note

    def display(self, name):
        """
        Display specific records
        :return: None
        """
        note = self.search(name)
        if note:
            note.print()
        else:
            print(f'There is no records for name {name}')

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
        for _ in range(randint(1, 4)):
            tag = Tag(tags_names[randint(1, len(tags_names)-1)])
            tags.append(tag)

        note = Note(name=name, text=text, tags=tags)
        book.add(note)
    return book


if __name__ == '__main__':
    fake = Faker()

    tags_names = []
    for i in range(10):
        tags_names.append(fake.text(
                max_nb_chars=Tag.max_tag_length)[:-1].replace(' ', '').lower())

    book = fake_records(NoteBook())
    book.display_all()
    tag = input('input tag > ')
    book.search(tag)
    # book.display_all()
    # book.save('contactbook.json')
