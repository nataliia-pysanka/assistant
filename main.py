import readline
readline.parse_and_bind("tab: complete")


def complete(text,state):
    volcab = ['dog', 'cat','rabbit','bird','slug','snail']
    results = [x for x in volcab if x.startswith(text)] + [None]
    return results[state]


readline.set_completer(complete)

line = input('prompt> ')

class Phone(Field):
    def __init__(self, value) -> None:
        super().__init__(value)
        self.__value = None
        self.value = value

    @property
    def phone(self):
        return self.__value

    @phone.setter
    def phone(self, value):
        try:
            value.isdigit()
        except:
            raise ValueError("Value Error, phone should contain numbers")
        self.__value = value
