with open("data",mode="w") as f:
    name="Mehmet Can"
    surname="Çakıt"
    gender="male"
    username="memocanx"
    job="programmer"
    f.write(f"Name: {name}\nSurname : {surname}\nGender: {gender}\nUsername: {username}\nJob: {job}")
with open("data",mode="r") as f:
    lines=f.read().splitlines()
    for i in range (len(lines)):
        lines[i]=lines[i].split(": ")
dic={}
for i in range (len(lines)):
    dic[lines[i][0]]=lines[i][1]
print(dic)