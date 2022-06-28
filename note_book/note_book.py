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


class NoteBook(UserDict):

    def __init__(self):
        super().__init__()
        self.counter = 0

    def add(self, note: Note):
        key = note.name
        self.data[key] = note

    def search(self, tag: str):
        for note in self.data.values():
            if tag in note.tag:
                print(note)

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
    for i in range(1):
        name = Name(fake.text(max_nb_chars=Name.max_name_length)[:-1])
        text = Text(fake.text(max_nb_chars=Text.max_text_length)[:-1])
        tags = []
        for _ in range(randint(1, 5)):
            tag = Tag(fake.text(
                max_nb_chars=Tag.max_tag_length)[:-1].replace(' ', ''))
            tags.append(tag)

        note = Note(name=name, text=text, tags=tags)
        book.add(note)
    return book


if __name__ == '__main__':
    fake = Faker()

    book = fake_records(NoteBook())
    book.display_all()
    # book.save('contactbook.json')
