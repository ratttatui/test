for i in range(1,5,1):
    nub = 0
    for j in range(1,i+1,1):
        if i % j == 0 :
            nub = nub + 1
    if nub == 2:
        print(f"Hello {i} is prime number!")
    elif i % 2 == 0:
        print(f"Hello {i} is even number!")
    else:
        print(f"Hello {i} is odd number!")