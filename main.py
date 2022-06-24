import readline
readline.parse_and_bind("tab: complete")


def complete(text,state):
    volcab = ['dog', 'cat','rabbit','bird','slug','snail']
    results = [x for x in volcab if x.startswith(text)] + [None]
    return results[state]


readline.set_completer(complete)

line = input('prompt> ')
