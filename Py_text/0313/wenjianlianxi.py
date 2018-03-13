import os
os.mkdir("./test")
os.chdir("./test")
for i in range(1,7):
    open("movie_"+str(i)+".avi","w")
list_dir=os.listdir("./")
for x in list_dir:
    oldname=x
    newname="[am]"+oldname
    os.rename(oldname,newname)