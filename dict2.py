# Wap to print all items in the dictionary separately

info = { "name ":"Chetan", "Age": 31, "Books_Liked":["Book1", "Book2","Book3"]}

'''
Expected output :
Chetan
31
Book1
Book2
Book3
'''

for i in info:
    if i == "Books_Liked":
        j = 0
        x = info["Books_Liked"][::-1]
        while j<= len(x)+1:

            g = x.pop()
            print(g)
            j +=1
    else:
        print(info[i])