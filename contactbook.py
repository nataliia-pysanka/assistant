from datetime import date
from notebook import * # in final version change * to final func calls


commands = {add_command:'add',       
            show_all_command: 'show all',
            days_to_birthday: 'days left',
            find_phone_command:'find phone',
            change_phone_command:'change phone',
            back_command:'main menu',
            #optional section
            change_birthday_command:'change birthday',
            change_name_command:'change name',
            change_email_command:'change email'
}

def parser(user_input: str):
  for command, input in commands.items():
    for elem in input:
      if user_input.lower().startswith(elem.lower()):
        data = user_input[len(elem):].strip().split(' ')
        return command, data


#Program starting func
def initial_main():
    while True:
        main_user_input = input('To enter contactbook please enter "1"\n'
                            'To enter notebook please enter "2"\n'
                            'To mantain your files please enter "3"\n'
                            'To exit program please enter "4"\n')
        match main_user_input:
          case '1': # Entering contactbook content
            contact_book_main()
          case '2': # Entering notebook content
            note_book_main()
          case '3': # Entering file mantaining content
            pass
          case '4': # Terminating programm
           break


#Contact book starting func
def contact_book_main():
    user_input = input('Please enter your command. Avaliable options are:\n'
    '-----> "add"<----- If you use this option, add contact name, optional info - phone, birth date, e-mail\n'
    '-----> "show all"<----- If you use this option, no extra input required\n'
    '-----> "days left"<----- If you use this option, add contact name\n'
    '-----> "find phone"<----- If you use this option, add contact name\n'
    '-----> "change phone"<----- If you use this option, add contact name, phone number you whant to change --> desired phone number\n'
    '-----> "main menu"<----- If you use this option, you will be sent to main menu\n'
    '-----> "change birthday"<----- If you use this option, add contact name,  desired birth date\n'
    '-----> "change name"<----- If you use this option, add existing contact name, desired contact name\n'
    '-----> "change email"<----- If you use this option, add existing e-mail, desired e-mail\n')
    command, data = parser(user_input)
    #command - future function call (add_command, find_phone_command.. etc)
    print(command(*data))
    if result is back_command:
         initial_main()
    user_input = input('Please enter your command. Avaliable options are:\n'
    '-----> "add"<----- If you use this option, add contact name, optional info - phone, birth date, e-mail\n'
    '-----> "show all"<----- If you use this option, no extra input required\n'
    '-----> "days left"<----- If you use this option, add contact name\n'
    '-----> "find phone"<----- If you use this option, add contact name\n'
    '-----> "change phone"<----- If you use this option, add contact name, phone number you whant to change --> desired phone number\n'
    '-----> "main menu"<----- If you use this option, you will be sent to main menu\n'
    '-----> "change birthday"<----- If you use this option, add contact name,  desired birth date\n'
    '-----> "change name"<----- If you use this option, add existing contact name, desired contact name\n'
    '-----> "change email"<----- If you use this option, add existing e-mail, desired e-mail\n')

