from contact_book.contactbook_menu import contact_book_main
from note_book.note_book import note_book_main


def initial_main():
    while True:
        main_user_input = input('To enter contactbook please enter "1"\n'
                                'To enter notebook please enter "2"\n'
                                'To mantain your files please enter "3"\n'
                                'To exit program please enter "4"\n')
        match main_user_input:
            case '1':  # Entering contactbook content
                contact_book_main()
            case '2':  # Entering notebook content
                note_book_main()
            case '3':  # Entering file mantaining content
                pass
            case '4':  # Terminating programm
                break


if __name__ == '__main__':
    initial_main()