dic = {0:0,1:0,2:0,3:0,4:0,5:0}

a = "110235120"

for i in a:
    i = int(i)
    dic[i] = dic[i] + 1
print(dic)