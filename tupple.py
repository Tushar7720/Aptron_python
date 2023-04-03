#lists in tupple

user = ("chetan",31,["Book1","Book2"])
user[2].append("Book3")
print(user)

for i in range(3):
    if i < 2:
        print(user[i])
    else:
        j =0
        while j < len(user[i]):
            print(user[i][j])
            j+=1
            