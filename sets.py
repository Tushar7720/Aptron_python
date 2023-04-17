#wap to demonstarte sets
s = { 1, 2 ,3, 4,5 ,6}
print(type(s))
print(max(s))
print(min(s))
s1 = s.intersection({2,3})
print(s1)
s1 = s.union({2,3})
print(s1)

s2 = { 7,8,9,12}

print(s.isdisjoint(s2))