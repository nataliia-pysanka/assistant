from collections import UserDict
import json
#from faker import Faker
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
        return f"{self._value}"


class Tag(Field):
    max_tag_length = 10
    allowed_chars = set(
        '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

    @Field.value.setter
    def value(self, value: str) -> None:
        """
        Tag validation and character limit
        """
        if not set(value).issubset(Tag.allowed_chars):
            raise ValueError(f"Incorrect characters in tag")
        elif len(value) > Tag.max_tag_length:
            raise ValueError(f"Tags cant be less than {Tag.max_tag_length} characters")
        self._value = value


class Text(Field):
    max_text_length = 200

    @Field.value.setter
    def value(self, value: str):
        """
        Character limit for the note content
        """
        if len(value) > 200:
            raise ValueError(f"Text can't be less than {Text.max_text_length} "
                             f"characters")
        self._value = value


class Name(Field):
    max_name_length = 15

    @Field.value.setter
    def value(self, new_value: str):
        """
        Character limit for the Name parameter
        """
        if len(new_value) > Name.max_name_length:
            raise ValueError(f"Name should contain under "
                             f"{Name.max_name_length} characters")
        Field.value.fset(self, new_value)

    def __str__(self):
        return f'{self.value}'

class Note:
    """
    Class for instance Note
    """

    def __init__(self, name: Name, text: Text = None, tags: List[Tag] = None):
        self.name = name
        self.tags = tags if tags else []
        self.text = text if text else None

    def add_tag(self, new_tag: Tag):
        """
        Validate and add new tag to the notebook
        :param new_tag: Tag
        """
        if not isinstance(new_tag, Tag):
            raise TypeError('\t Tag can not be added \n')
        if len(self.tags) == 4:
            raise ValueError('\t Too mach tags already \n')
        if new_tag.value not in self.tags:
            self.tags.append(new_tag)
            return new_tag

    def add_text(self, new_txt: Text):
        """
        Validate and add new note content to the notebook
        :param new_txt: Text
        """
        if not isinstance(new_txt, Text):
            raise TypeError('\t Text can not be added \n')
        if not self.text:
            self.text = new_txt

    def delete_tag(self, tag: Tag):
        """
        Validate and remove specific tag from the notebook
        :param new_tag: Tag
        """
        if not isinstance(tag, Tag):
            raise TypeError('\t Incorrect type of tag \n')
        if tag in self.tags:
            self.tags.remove(tag)
        else:
            print(f'\t The tag {tag} is not found \n')

    # def delete_note(self, arg):
    # """
    # Delete specific note cand validation
    # """
    #     notebook = NoteBook()
    #     if arg in notebook.data.keys():
    #         del notebook.data[arg]
    #         print(f'Note deleted')
    #         notebook.save()
    #     else:
    #         print("Couldn't find the note)\n")

    # def edit_note(self, text: Text, new_txt: Text):
    # """
    # Change note content and validation
    # :param text: Text, new_txt: Text
    # """
    #     if not isinstance(text, Text):
    #         print('\t Note not found, please enter correctly \n')
    #         return

    #     note_in_list = self.number_in_list(text)
    #     if note_in_list:
    #         note_in_list.value = new_txt.value
    #         return
    #     raise ValueError('\t The note was not found \n')

    # def note_in_list(self, text: Text):
    # """
    # Get note position for edit_note function
    # :param text: Text
    # """
    #     for pl in self.text:
    #         if text.value == pl.value:
    #             return pl

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

    def serealize(self):
        """
        Transform data from object Note to the dictionary
        :return: dict
        """
        dump = {}
        if self.name:
            dump['name'] = self.name.value
        tags_for_dump = []
        if self.tags:
            for tag in self.tags:
                tags_for_dump.append(tag.value)
            dump['tags'] = tags_for_dump
        if self.text:
            dump['text'] = self.text.value
        return dump

    def deserealize(self, note):
        """
        Transform data from dictionary to object Note
        :return: dict
        """
        if note['name']:
            self.name.value = note['name']
        if note['text']:
            self.add_text(Text(note['text']))
        if note['tags']:
            for tag in note['tags']:
                self.add_tag(Tag(tag))



class NoteBook(UserDict):
    """
    Class-container for different note records
    """
    def __init__(self):
        super().__init__()
        self.counter = 0


    def add(self, note: Note):
        """
        Add new record to the storage
        :param note: Note
        """
        key = note.name.value
        self.data[key] = note
        print(self.data.keys())

    def add_tag(self, name: str, tag_obj: Tag):
        note = self.search(name)
        if note:
            try:
                note.add_tag(tag_obj)
            except ValueError as err:
                print(err)

    def search_tag(self, tag: str):
        for note in self.data.values():
            if note.has_tag(tag):
                note.print()

    def delete(self, note: Note):
        if note.name in self.data:
            del self.data[note.name]

    # def edit_note(self, name: Name, new_note: Note) -> str:
    # """
    # Edit note content notebook
    # :param name: Name, new_note: Note
    # """
    #     self.data[name] = new_note

    # def find(self, param: str):
    # """
    # Search notes by user input and validatoin
    # :param param: str
    # """
    #     if len(param) < 3:
    #         raise ValueError("Param for find must be eq or grater than 3 symbols.")
    #
    #     notebook = NoteBook()
    #
    #     for k, v in self.items():
    #         if param.lower() in k.lower() or [p.value for p in v.data if param in p.value]:
    #             notebook.add(v)
    #             continue
    #     return notebook

    # def sort_by_tag(self, tag: Tag):
    # """
    # Sort notes by tags
    # :param tag: Tag
    # """
    #     notebook = NoteBook()
    #     sorted_tags = sorted(notebook, key=itemgetter('tag'))


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

    def save(self, filename: str):
        dump = []
        for name, note in self.data.items():
            dump.append(note.serealize())
        with open(filename, 'w', encoding='UTF-8') as f:
            json.dump(dump, f)

    def load(self, filename: str):
        self.clear()
        with open(filename, 'r', encoding='UTF-8') as f:
            dump = json.load(f)
        for note in dump:
            txt = Note(name=Name('none'))
            txt.deserealize(note)
            self.add(txt)

    def clear(self):
        """
        Clear all the data in the ContactBook
        :return:
        """
        self.data = {}


# def fake_records(book: NoteBook):
#     for i in range(50):
#         name = Name(fake.text(max_nb_chars=Name.max_name_length)[:-1])
#         text = Text(fake.text(max_nb_chars=Text.max_text_length)[:-1])
#         tags = []
#         for _ in range(randint(1, 4)):
#             tag = Tag(tags_names[randint(1, len(tags_names)-1)])
#             tags.append(tag)
#
#         note = Note(name=name, text=text, tags=tags)
#         book.add(note)
#     return book


if __name__ == '__main__':

    # fake = Faker()

    # tags_names = []
    # for i in range(10):
    #     tags_names.append(fake.text(
    #             max_nb_chars=Tag.max_tag_length)[:-1].replace(' ', '').lower())

    # book = fake_records(NoteBook())
    # book.display_all()
    # book.save('notebook.json')
    # book = NoteBook()
    # book.load('notebook.json')
    # book.display_all()
    # book.display_all()
    # book.save('contactbook.json')
