from classes.Book import Book


def main():
    first_book = Book(title="Influence: The Psychology of Persuasion", author="Robert Chialdini", amount_of_pages=186,
                      price_in_hrn=150, publishing_company="Globus", publishing_year=2019)
    second_book = Book(title="Elon Musk", author="Ashlee Vance", amount_of_pages=402, price_in_hrn=250,
                       publishing_company="Virgin Books")
    third_book = Book(title="The Grand Design", author="Stephen Hawking and Leonard Mlodinow", amount_of_pages=206)

    print(first_book.__str__())
    print(second_book.__str__())
    print(third_book.__str__())


if __name__ == '__main__':
    main()
