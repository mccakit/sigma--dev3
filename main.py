with open("data.txt",mode="w") as f:
    name=input("What is your name")
    surname=input("What is your surname")
    gender=input("What is your gender")
    username=input("What is your username")
    job=input("Your dream job")
    f.write(f"Name: {name}\nSurname : {surname}\nGender: {gender}\nUsername: {username}\nJob: {job}")
with open("data.txt",mode="r") as f:
    lines=f.read().splitlines()
    for i in range (len(lines)):
        lines[i]=lines[i].split(": ")
dic={}
for i in range (len(lines)):
    dic[lines[i][0]]=lines[i][1]
print(dic)