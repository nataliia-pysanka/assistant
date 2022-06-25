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
        self._value = value


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

    def __init__(self, name, birthday, phone):
        self.name = name
        self.birthday = birthday
        self.phone = phone

    def __str__(self):
        rec = '\t {:<8}...{:<15}'.format('........', '...............') + '\n'
        rec += '\t {:<8} : {:<15}'.format('Name', self.name) + '\n'
        rec += '\t {:<8} : {:<15}'.format('Birthday', self.birthday) + '\n'
        rec += '\t {:<8}...{:<15}'.format('........', '...............') + '\n'
        rec += '\t {:<8} : {:<15}'.format('Number', self.phone) + '\n'
        rec += '\t {:<8}...{:<15}'.format('........', '...............') + '\n'
        return rec