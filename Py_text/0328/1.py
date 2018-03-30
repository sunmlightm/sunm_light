class Students(object):
    # 定义初始化属性
    def __init__(self,name,id,clas):
        self.name=name
        self.id=id
        self.clas=clas
        self.book_list=[]

    # 借书
    def take_book(self,book):
        self.book_list.append(book)
        print("学生:%s 已借到:%s 作者:%s"%(self.name,book.name,book.author))

    # 还书
    def return_book(self,book):
        if book in self.book_list:
            self.book_list.remove(book)
            print("归还:%s"%book.name)
        else:
            print("没有借那本书")

    # 保存到本地
    def save_books(self):
        str1 = ""
        for book in self.book_list:
            str1 += book.name
        f=open("booklist.txt","w")
        f.write(str1)
        f.close()


class Books(object):
    # 定义初始化属性
    def __init__(self,name,author):
        self.name=name
        self.author=author

st1=Students("wukong","100","0102")
book1=Books("xiyouji","tangseng")
st1.take_book(book1)
st1.save_books()
st1.return_book(book1)
