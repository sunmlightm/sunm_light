import os,shutil
num=0
result=os.listdir("./")
for x in result:
    if x.endswith(".py"):
        num+=1
    else:
        if x.rfind(".")==-1:
            shutil.rmtree(x)
        else:
            os.remove(x)