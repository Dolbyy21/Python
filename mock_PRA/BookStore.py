class Book:
    def __init___(self, pages, price, author, id1, title):
        self.pages = pages
        self.price = price
        self.author = author
        self.id1 = id1
        self.title = title
class BookStore:
    def __init__(self, book_store_name, book_list):
        self.book_list = book_list
        self.book_store_name = book_store_name
    
    def find_minimum_team_by_Id(self):
        minim = 999999
        obj = None
        for each in self.book_list:
            if each.id1 < minim:
                minim = each.id1
                obj = each
        return obj
    def sort_book_by_Id(self):
        l = []
        for each in self.book_list:
            l.apped(each.id1)
        return sorted(l) if len(l)!=0 else None
n = int(input())
l = []
for i in range(n):
    pages = int(input())
    price = int(input())
    author = input()
    id1 = int(input())
    title = input()
    l.append(Book(pages,price,author,id1,title))
obj = BookStore("",l)
x = obj.find_minimum_team_by_Id()
if x == None:
    print("No Data Found")
else:
    print(x.pages)
    print(x.price)
    print(x.author)
    print(x.id1)
    print(x.title)
y = obj.sort_book_by_Id()
if y == None:
    print("No Data Found")
else:
    for i in y:
        print(i)
        