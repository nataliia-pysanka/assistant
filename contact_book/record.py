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

    def __str__(self):
        if self._value:
            return self._value
        return ''


class Birthday(Field):

    def __init__(self, birth: str):
        self._value = None
        self.value = birth

    @Field.value.setter
    def value(self, data):
        try:
            self._value = datetime.strptime(data, '%d.%m.%Y').date()
        except ValueError:
            print(
                "Birthday format issue. Please enter birthday in DD.MM.YY format")

    @property
    def value_as_str(self):
        if self.value:
            return self.value.strftime('%d.%m.%Y')

    def days_to_birthday(self):
        if not self.value:
            return None
        day_now = datetime.now().date()
        current_year = self.value.replace(year=day_now.year)
        if current_year > day_now:
            delta = current_year - day_now
            print(f'You have left {delta.days} to next birthday!')
            return delta
        else:
            next_b_day = current_year.replace(year=day_now.year + 1)
            delta = next_b_day - day_now
            print(f'You have left {delta.days} to next birthday!')
            return delta


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
    def value(self, value: str):
        num = (value.strip().removeprefix('+')
               .replace("(", '')
               .replace(")", '')
               .replace(" ", '')
               .replace("-", ''))
        if not num.isdigit():
            raise ValueError("Value Error, phone should contain numbers")

        if len(num) not in (10, 12):
            raise ValueError("Value Error, operator not valid")

        operators = {"067", "068", "096", "097", "098",
                     "050", "066", "095", "099", "063", "073", "093"}

        if len(num) == 12 and num[:2] == '38':
            num = num[2:]

        if num[:3] not in operators:
            raise ValueError("Value Error, operator not valid")

        self._value = num

class Email(Field):

    def __init__(self, value: str = '') -> None:
        super().__init__(value)

    @Field.value.setter
    def value(self, value: str) -> None:
        pattern = r"[a-zA-Z]+[a-zA-Z0-9._]+@[a-z]+\.[a-z]{2,}"
        if re.match(pattern, value):
            Field.value.fset(self, value)
        else:
            raise ValueError("Please, enter a valid email" +
                             "Example: example@***.***")


class Record:
    """
    Class for instance Record
    """

    def __init__(self, name: Name, num: Phone = None,
                 birthday: Birthday = None, email: Email = None) -> None:
        self._name = None
        self.name = name
        self.birthday = birthday
        self.nums = []
        if num:
            self.nums.append(num)
        self.emails = []
        if email:
            self.emails.append(email)

    def __str__(self):
        return f'NAME: {self.name}\n' \
               f'BIRTHDAY: {self.birthday}\n'

    def print(self):
        rec = f'\t {"." * 30} \n'
        rec += '\t  {:<8} : {:<15}'.format('NAME', str(self.name)) + '\n'

        birth = str(self.birthday) if self.birthday else ''
        rec += '\t  {:<8} : {:<15}'.format('BIRTHDAY', birth) + '\n'

        indx = 1
        for phone in self.nums:
            rec += '\t  {:<8} : {:<15}'.format(f'NUMBER {indx}',
                                               str(phone.value)) + '\n'
            indx += 1

        indx = 1
        for email in self.emails:
            rec += '\t  {:<8} : {:<15}'.format(f'EMAIL {indx}',
                                               str(email)) + '\n'
            indx += 1
        rec += f'\t {"." * 30} \n'
        print(rec)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name: Name):
        self._name = new_name

    @property
    def numbers(self):
        if self.nums:
            return self.nums

    @property
    def e_mails(self):
        if self.emails:
            return self.emails

    def add_email(self, new_email: Email):
        if not isinstance(new_email, Email):
            print('\t Number not added, Phone entered incorrectly \n')
            return
        email_in_list = self.email_in_list(new_email)
        if email_in_list:
            print(f'\t Number {new_email.value} already exist')
            return
        self.emails.append(new_email)
        return new_email

    def add_phone(self, new_num: Phone):
        if not isinstance(new_num, Phone):
            print('\t Number not added, Phone entered incorrectly \n')
            return
        number_in_list = self.number_in_list(new_num)
        if number_in_list:
            print(f'\t Number {new_num.value} already exist')
            return
        self.nums.append(new_num)
        return new_num

    def remove_phone(self, num: Phone):
        if not isinstance(num, Phone):
            print('\t Number not identified, Phone entered incorrectly \n')
            return

        number_in_list = self.number_in_list(num)
        if number_in_list:
            self.nums.remove(number_in_list)
            return number_in_list
        raise ValueError(f'\t Number {num.value} is not found \n')

    def edit_phone(self, num: Phone, new_num: Phone):
        if not isinstance(num, Phone):
            print('\t Number not found, please enter correctly \n')
            return

        number_in_list = self.number_in_list(num)
        if number_in_list:
            number_in_list.value = new_num.value
            return
        raise ValueError(f'\t The number {num.value} is not found \n')

    def number_in_list(self, num: Phone):
        for number in self.nums:
            if num.value == number.value:
                return number

    def email_in_list(self, mail: Email):
        for email in self.emails:
            if mail.value == email.value:
                return email

    def get_phone(self, num: str) -> Phone:
        for number in self.nums:
            if num == number.value:
                return number

    def get_email(self, email: str) -> Email:
        for mail in self.emails:
            if email == mail.value:
                return mail

    def serealize(self):
        """
        Transform data from object Record to the dictionary
        :return: dict
        """
        dump = {}
        for key, value in self.__dict__.items():
            dump.update({key: value})
        return dump

    def deserealize(self, record):
        """
        Transform data from dictionary to object Record
        :return: dict
        """
        for key, value in record.items():
            self.__dict__[key] = value

    def __repr__(self):
        return f'{", ".join([p.value for p in self.nums])}'


# if __name__ == "__main__":
#     e = Email('first@go.com')
#     print(e)
#     rec = Record(name='Kim', email=e)
#     rec.print()
#     rec.add_email(e)
#     rec.print()
#     try:
#         rec.add_phone(Phone('088765432'))
#     except ValueError as err:
#         print(err)
#     print(rec)
#     rec.add_phone(Phone('066-765-43-36'))
#     rec.add_phone(Phone('+38(095)654-34-23'))
#     rec.print()
    # rec.add_email(Email('hello@ukr.net'))
    # rec.add_email(Email('go@gmail.com'))
    # print(rec.get_phone('088765434'))
    # rec.print()
    # rec.remove_phone(Phone('088765434'))
    # rec.print()
    # rec.edit_phone(Phone('088765433'), Phone('999'))
    # rec.print()
    #
    # b = Birthday('01.01.2000')
    # print(b.value_as_str)
    #
    # print(b.days_to_birthday())
    # rec.remove_phone(Phone('088765434'))
