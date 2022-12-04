with open("data.txt") as f:
    mylist = f.read().splitlines()
for n in range(len(mylist)):
    mylist[n]=mylist[n].split(": ")
dic={}
for temp1 in range (len(mylist)):
    dic[mylist[temp1][0]]=mylist[temp1][1]
print(dic)
f.close()