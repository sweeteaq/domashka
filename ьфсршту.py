class Book():
    def __init__(self,title,author,year,pages):
        self.title=title
        self.author=author
        self.year=year
        self.pages=pages
    def info(self):
        print('Название',self.title)
        print("Автор",self.author)
        print('Год издания',self.year)
        print('Колличество страниц',self.pages)
    def new_pages(self, pages):
        self.pages = pages
    def __str__(self):
        return f'self.title,self.author,self.year,self.pages'
example_book=Book("Дежавю",'Олегий',1337,228)
example_book.info()
example_book.new_pages()
example_book.info()
print(example_book)