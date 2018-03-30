def text(num):
    print("text_out:"+str(num))
    a=1
    def text_in():
        print("text_in")
        return a
    return text_in

text=text(10)
print(text())