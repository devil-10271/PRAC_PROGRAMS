class library:
    def __init__(self,n_o_f=0,book1=None):
        self.NOF=n_o_f
        self.books=book1

    def checks(self):
        if(len(self.books)!=self.NOF):
            print('\n\nCode error')
        else :
            print('\n\nno error in code')

books=list()
no_of_books=int(input('how many books to insert into library : '.capitalize()))
for i in range(no_of_books):
    book=input(f'enter book {i+1} name : '.title())
    books.append(book)

a=library(no_of_books,books)
a.checks()