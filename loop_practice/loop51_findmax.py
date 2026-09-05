import random
li = random.sample(range(1,101),10)
print(li)

# paper1 = li[0]

# ##1
# li.pop(0)

##2
##li = li[1::]

mem = 0

for i in li:
    if mem > i:
        pass
    else:
        mem = i

print(mem)


a = min(li)
print(a)