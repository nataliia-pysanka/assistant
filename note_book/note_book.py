from collections import UserDict
import json
# from faker import Faker


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


class Tag(Field):
    max_tag_length = 10
    allowed_chars = set(
        '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

    @Field.value.setter
    def value(self, value: str) -> None:
        if not set(value).issubset(Tag.allowed_chars):
            print(f"Tags can only be under {Tag.max_tag_length} characters")
            return
        elif len(value) < Tag.max_tag_length:
            print(f"Tags can be less than {Tag.max_tag_length} characters")
            return
        self._value = value

    def __str__(self) -> str:
        return self.value


class Text(Field):
    max_text_length = 200

    @Field.value.setter
    def value(self, value: str):
        if len(value) > 200:
            print(f"Text can be less than {Text.max_text_length} characters")
            return
        self._value = value

    def __str__(self) -> str:
        return self.value


class Name(Field):
    max_name_length = 15

    @Field.value.setter
    def value(self, value: str):
        if len(value) < Name.max_name_length:
            print(f"Name should contain under {Name.max_name_length} "
                  f"characters")
            return
        self._value = value

    def __str__(self) -> str:
        return self.value


class Note:

    def __init__(self, name: Name, tag: Tag = None, txt: Text = None) -> None:
        self.tags = []
        self.text = txt
        if tag:
            self.tags.append(tag)

    def add_tag(self, new_tag: Tag):
        if not isinstance(new_tag, Tag):
            print('\t Tag can not be added \n')
            return
        if new_tag.value not in self.tags:
            self.tags.append(new_tag)
            return new_tag

    def add_text(self, new_txt: Text):
        if not isinstance(new_txt, Text):
            print('\t Tag can not be added \n')
            return
        if new_txt.value not in self.data:
            self.data.update(new_txt)
            return new_txt

    def delete_note(self, arg):
        if arg in notebook.data.keys():
            del notebook.data[arg]
            print(f'Note deleted')
            notebook.save()
        else:
            print("Couldn't find the note)\n")

    def delete_tag(self, tag):
        if tag.value in [t.value for t in self.tags]:
            self.tags.remove(tag)


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

    def edit_note(self, name: Name, new_note: Note) -> str:
        self.data[name] = new_note

    def find(self, param: str):

        if len(param) < 3:
            raise ValueError("Param for find must be eq or grater than 3 symbols.")

        notebook = NoteBook()

        for k, v in self.items():
            if param.lower() in k.lower() or [p.value for p in v.data if param in p.value]:
                notebook.add(v)
                continue
        return notebook

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

    def __str__(self) -> str:
        result = "\n".join([str(rec) for rec in self.data.values()])
        return result

#notebook = NoteBook()

#notebook.load()

def show_all():
    nb = str(notebook)
    if len(nb) == 0:
        print('No notes to show')
    else:
        print(nb)

def change_note():
    choose_note = input("Enter needed topic to change:\n")
    if choose_note not in notebook.data.keys():
        print("Note not found")
    else:
        new_txt = input("Enter new note:\n")
        notebook.edit_note(choose_note, Note(Name(choose_note), Note(new_txt)))
        notebook.save()
        print("Note changed")

if __name__ == '__main__':
    note = Note(name = Name('something'), tag = Tag('dtt'), txt = Text('ttt gggg'))

