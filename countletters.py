#wap to count occurance of letters in a s string and store as key value pairs in a dict

count={}
string_input = "My name is tushar agarwal"
for i in string_input:
    count[i]=string_input.count(i)
print(count)