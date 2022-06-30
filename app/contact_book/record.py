import re
from datetime import datetime


class Field:

    def __init__(self, value: str) -> None:
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if not value:
            self._value = None
            return
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
        """
        Validate given Birthday format
        """
        if not data:
            self._value = None
            return
        try:
            self._value = datetime.strptime(data, '%d.%m.%Y').date()
        except ValueError:
            print("Birthday format issue. Please enter birthday in "
                  "DD.MM.YY format")

    @property
    def value_as_str(self):
        if self.value:
            return self.value.strftime('%d.%m.%Y')

    def days_to_birthday(self):
        """
        Count number of days till specific person's Birthday
        """
        if not self.value:
            return None
        day_now = datetime.now().date()
        current_year = self.value.replace(year=day_now.year)
        if current_year > day_now:
            delta = current_year - day_now
            return(f'You have left {delta.days} day(s) to next birthday!')
            # return delta
        else:
            next_b_day = current_year.replace(year=day_now.year + 1)
            delta = next_b_day - day_now
            return(f'You have left {delta.days} day(s)to next birthday!')
            # return delta


class Name(Field):

    def __init__(self, value: str) -> None:
        super().__init__(value)

    @Field.value.setter
    def value(self, value: str):
        """
        Validate given name
        """
        if not value:
            raise ValueError('Name is obligatory parameter')
        if not isinstance(value, str):
            raise ValueError("Name should be a string")
        self._value = value


class Phone(Field):

    def __init__(self, value) -> None:
        super().__init__(value)

    @Field.value.setter
    def value(self, value: str):
        """
        Validate and sanitize given phone number
        """
        if not value:
            self._value = None
            return
        num = (value.strip().removeprefix('+')
               .replace("(", '')
               .replace(")", '')
               .replace(" ", '')
               .replace("-", ''))
        if not num.isdigit():
            raise ValueError("Value Error, phone should contain numbers")

        if len(num) not in (10, 12):
            raise ValueError("Value Error, phone length should be 12 symbols")

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
        """
        Validate given email
        """
        if not value:
            self._value = None
            return
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
        """
        Display all available records
        :return: None
        """
        rec = f'\t {"." * 30} \n'
        rec += '\t  {:<8} : {:<15}'.format('NAME', str(self.name.value)) + '\n'

        if self.birthday:
            birth = str(self.birthday.value)
        else:
            birth = ''
        rec += '\t  {:<8} : {:<15}'.format('BIRTHDAY', birth) + '\n'

        for phone in self.nums:
            num = str(phone.value) if phone.value else ''
            rec += '\t  {:<8} : {:<15}'.format(f'NUMBER', num) + '\n'

        for email in self.emails:
            mail = str(email.value) if email.value else ''
            rec += '\t  {:<8} : {:<15}'.format(f'EMAIL', mail) + '\n'
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
        """
        Validate and add new email to the record
        :param new_email: Email
        """
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
        """
        Validate and add new phone to the record
        :param new_num: Phone
        """
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
        """
        Validate and remove phone from the record
        :param num: Phone
        """
        if not isinstance(num, Phone):
            print('\t Number not identified, Phone entered incorrectly \n')
            return

        number_in_list = self.number_in_list(num)
        if number_in_list:
            self.nums.remove(number_in_list)
            return number_in_list
        raise ValueError(f'\t Number {num.value} is not found \n')

    def edit_phone(self, num: Phone, new_num: Phone):
        """
        Validate and edit specific phone number from the record
        :param num: Phone, new_num: Phone
        """
        if not isinstance(num, Phone):
            print('\t Number not found, please enter correctly \n')
            return

        number_in_list = self.number_in_list(num)
        if number_in_list:
            number_in_list.value = new_num.value
            return
        raise ValueError(f'\t The number {num.value} is not found \n')

    def number_in_list(self, num: Phone):
        """
        Get phone number position for working with phone functions
        :param num: Phone
        """
        for number in self.nums:
            if num.value == number.value:
                return number

    def get_phone(self, num: str) -> Phone:
        """
        Get specific phone number
        :param num: Email
        """
        for number in self.nums:
            if num == number.value:
                return number

    def get_email(self, email: str) -> Email:
        """
        Get specific email
        :param email: Email
        """
        for mail in self.emails:
            if email == mail.value:
                return mail

    def serealize(self):
        """
        Transform data from object Record to the dictionary
        :return: dict
        """
        dump = {}
        if self.name:
            dump['name'] = self.name.value

        if self.birthday:
            dump['birthday'] = self.birthday.value_as_str

        phone_for_dump = []
        if self.nums:
            for num in self.nums:
                phone_for_dump.append(num.value)
            dump['nums'] = phone_for_dump

        email_for_dump = []
        if self.emails:
            for mail in self.emails:
                email_for_dump.append(mail.value)
            dump['emails'] = email_for_dump
        return dump

    def deserealize(self, record):
        """
        Transform data from dictionary to object Record
        :return: dict
        """
        if record['name']:
            self.name.value = record['name']

        if record.get('birthday'):
            self.birthday = Birthday(record['birthday'])

        if record.get('nums'):
            for num in record['nums']:
                self.add_phone(Phone(num))

        if record.get('emails'):
            for email in record['emails']:
                self.add_email(Email(email))

    def __repr__(self):
        return f'{", ".join([p.value for p in self.nums])}'

    def edit_birthday(self, new_birthday: str):
        """
        Edit specific person's birthday
        :param new_birthday: str
        """
        if self.birthday:
            self.birthday.value = new_birthday
        else:
            self.birthday = Birthday(new_birthday)

    def edit_name(self, new_name: str):
        """
        Edit specific person's name
        :param new_name: str
        """
        self.name.value = new_name

    def email_in_list(self, mail: Email):
        """
        Get phone email position for working with email functions
        :param mail: Email
        """
        for email in self.emails:
            if mail.value == email.value:
                return email

    def edit_email(self, email: Email, new_email: Email):
        """
        Validate and edit specific person's email
        :param email: Email,
        :param new_email: Email
        """
        if not isinstance(email, Email):
            print('\t Email not found, please enter correctly \n')
            return

        mail_in_list = self.email_in_list(email)
        if mail_in_list:
            mail_in_list.value = new_email.value
            return
        raise ValueError(f'\t Email {email.value} is not found \n')
