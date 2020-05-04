class Book:
    book_site_link = "www.book.com"

    def __init__(self, title=None, author=None, amount_of_pages=None,
                 price_in_hrn=None, publishing_company=None, publishing_year=None):
        self.__amount_of_pages = amount_of_pages
        self.__author = author
        self.__price_in_hrn = price_in_hrn
        self.__title = title
        self.__publishing_company = publishing_company
        self.__publishing_year = publishing_year

    def __del__(self):
        print("Deleted " + self.__class__.__name__)

    def __repr__(self):
        return {'title': self.title,
                'author': self.author,
                'amount_of_pages': self.amount_of_pages,
                'price_in_hrn': self.price_in_hrn,
                'publishing_company': self.publishing_company,
                'publishing_year': self.publishing_year,
                'book_site_link': self.book_site_link}

    def __str__(self):
        return '\nTitle: "' + str(self.title) + \
               '"\nAuthor: ' + str(self.author) + \
               '\nPages: ' + str(self.amount_of_pages) + \
               '\nPrice in UAH: ' + str(self.price_in_hrn) + \
               '\nPublishing company: ' + str(self.publishing_company) + \
               '\nPublishing year: ' + str(self.publishing_year) + \
               '\nBook site link: ' + str(self.book_site_link) + "\n"

    @staticmethod
    def get_site():
        return Book.book_site_link

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def amount_of_pages(self):
        return self.__amount_of_pages

    @property
    def price_in_hrn(self):
        return self.__price_in_hrn

    @property
    def publishing_company(self):
        return self.__publishing_company

    @property
    def publishing_year(self):
        return self.__publishing_year

    @author.setter
    def author(self, author):
        self.__author = author

    @amount_of_pages.setter
    def amount_of_pages(self, amount_of_pages):
        self.__amount_of_pages = amount_of_pages

    @price_in_hrn.setter
    def price_in_hrn(self, price_in_hrn):
        self.__price_in_hrn = price_in_hrn

    @title.setter
    def title(self, title):
        self.__title = title

    @publishing_company.setter
    def publishing_company(self, publishing_company):
        self.__publishing_company = publishing_company

    @publishing_year.setter
    def publishing_year(self, publishing_year):
        self.__publishing_year = publishing_year
