import re

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
        self.__value = None
        self.value = value


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
        pattern = re.findall(r"[a-zA-Z]+[a-zA-Z0-9._]+@[a-z]+\.[a-z]{2,}"
        if re.match(pattern, value):
            Field.value.fset(self, value)
        else:
            raise ValueError("Please, enter a valid email" +
                             "Example: example@***.***")


class Record:

    def __init__(self, name: Name, num: Phone) -> None:    # + Birthday
        self.name = name
        self.nums = []
        if num:
            self.nums.append(num)


    def __repr__(self):
        return f'{", ".join([p.value for p in self.nums])}'
