class Test(object):
    def __init__(self,swtch_flg):
        self.swtch_flg=swtch_flg

    def calc_num(self,a,b):
        try:
            result=a/b
        except Exception as e:
            if self.swtch_flg:
                print("打印异常%s"%e)
            else:
                raise
        else:
            print("1")
Test(True).calc_num(2,0)