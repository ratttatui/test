dic = {0:0,1:0,2:0,3:0,4:0,5:0}

a = "110235120"

for i in a:
    i = int(i)
    dic[i] = dic[i]+1
    # if i == 1:
    #     dic[i] = dic[i]+1
    # if i == 2:
    #     dic[i] = dic[i]+1
    # if i == 3:
    #     dic[i] = dic[i]+1
    # if i == 4:
    #     dic[i] = dic[i]+1
    # if i == 5:
    #     dic[i] = dic[i]+1

print(dic)