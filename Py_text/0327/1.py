def test():
    print("test>1")
    a=100
    def test_in():
        nonlocal a
        a+=10
        print("in")
        def test2():
            print("2")
            return 2
        return test2()

    print("test>2")
    return test_in
t=test()
# print(t())
t()