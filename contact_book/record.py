import re
from datetime import datetime
from datetime import date

class Field:

    def __init__(self, value: str) -> None:
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


class Name(Field):

    def __init__(self, value: str) -> None:
        super().__init__(value)

    @Field.value.setter
    def value(self, value: str):
        if not isinstance(value, str):
            raise ValueError("Name should be a string")
        self._value = value


class Phone(Field):

    def __init__(self, value) -> None:
        super().__init__(value)

    @Field.value.setter
    def phone(self, value):
        try:
            value.isdigit()
        except:
            raise ValueError("Value Error, phone should contain numbers")
        self.__value = value


class Email(Field):

    def __init__(self, value: str = '') -> None:
        super().__init__(value)

    @Field.value.setter
    def value(self, value: str) -> None:
        pattern = re.findall(r"[a-zA-Z]+[a-zA-Z0-9._]+@[a-z]+\.[a-z]{2,}")
        if re.match(pattern, value):
            Field.value.fset(self, value)
        else:
            raise ValueError("Please, enter a valid email" +
                             "Example: example@***.***")


class Record:

    def __init__(self, name: Name, num: Phone = None) -> None:    # + Birthday
        self._name = None
        self.name = name
        self._nums = []
        if num:
            self.nums.append(num)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name: Name):
        self._name = new_name

    @property
    def numbers(self):
        if self._nums:
            return self._nums

    def add(self, new_num: Phone):
        if not isinstance(new_num, Phone):
            print('\t Number not added, Phone entered incorrectly \n')
            return
        if new_num.value not in [p.value for p in self.nums]:
            self.nums.append(new_num)
            return new_num

    def remove(self, num: Phone):
        if not isinstance(num, Phone):
            print('\t Number not identified, Phone entered incorrectly \n')
            return
        if num in self.nums:
            i = self.nums.index(num)
            return self.nums.pop(i)
        print(f'\t The number {num.value} is not found \n')

    def edit(self, num: Phone, new_num: Phone):
        if not isinstance(num, Phone):
            print('\t Number not found, please enter correctly \n')
            return
        if new_num not in self.nums:
            print(f'\t The number already exists \n')
            return

        self.remove(num)
        self.nums.append(new_num)

# + метод days_to_birthday

    def __repr__(self):
        return f'{", ".join([p.value for p in self.nums])}'