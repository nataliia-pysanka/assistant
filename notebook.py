commands = { add_note_command:'add note',
            add_tag_command:'add tag',
            change_text_command:'change text', # extra command, optional
            show_single_command:'show note', # executed after search_note or could be summoned on it's own
            show_all_command:'show all notes',
            search_note_command:'search note',
            delete_note_command:'erase note',
}


def parser(user_input: str):
  for command, input in commands.items():
    for elem in input:
      if user_input.lower().startswith(elem.lower()):
        data = user_input[len(elem):].strip().split(' ')
        return command, data

        
def note_book_main():
    user_input = input('Please enter your command. Avaliable options are:\n'
    '-----> "add note"<----- If you use this option, add contact name, optional info - phone, birth date, e-mail\n'
    '-----> "add tag"<----- If you use this option, no extra input required\n'
    '-----> "change text"<----- If you use this option, add contact name\n'
    '-----> "show note"<----- If you use this option, add contact name\n'
    '-----> "show all notes"<----- If you use this option, add contact name, phone number you whant to change --> desired phone number\n'
    '-----> "search note"<----- If you use this option, you will be sent to main menu\n'
    '-----> "erase note"<----- If you use this option, add contact name,  desired birth date\n')