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


class Birthday(Field):
    @Field.value.setter
    def value(self, data):
        try:
            self._value = datetime.strptime(data, '%d.%m.%Y').date()
        except:
            raise ValueError(
                "Birthday format issue. Please enter birthday in DD.MM.YY format")

    def days_to_birthday(self):
        if not self.b_day:
            return None
        day_now = datetime.now().date()
        current_year = self.b_day.param.replace(year=day_now.year)
        if current_year > day_now:
            delta = current_year - day_now
            print(f'You have left {delta.days} to next birthday!')
            return delta
        else:
            next_b_day = current_year.replace(year=day_now.year + 1)
            delta = next_b_day - day_now
            print(f'You have left {delta.days} to next birthday!')
            return delta


class Record:
    """
    Class for instance Record
    """

    def __init__(self, name: Name, birthday: Birthday, num: Phone = None) -> None:
        self._name = None
        self.name = name
        self.birthday = birthday
        self.num = num
        self._nums = []
        if num:
            self.nums.append(num)

    def __str__(self):
        rec = '\t {:<8}...{:<15}'.format('........', '...............') + '\n'
        rec += '\t {:<8} : {:<15}'.format('Name', self.name) + '\n'
        rec += '\t {:<8} : {:<15}'.format('Birthday', self.birthday) + '\n'
        rec += '\t {:<8}...{:<15}'.format('........', '...............') + '\n'
        rec += '\t {:<8} : {:<15}'.format('Number', self.num) + '\n'
        rec += '\t {:<8}...{:<15}'.format('........', '...............') + '\n'
        return rec

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

    def __repr__(self):
        return f'{", ".join([p.value for p in self.nums])}'


