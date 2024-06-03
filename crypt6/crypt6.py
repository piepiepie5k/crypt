def power(x, y, z):
    base = x
    pows = x
    ost = 1
    step = 1
    counter = 0
    counter_mp=0
    while y > 0:
        print(f"{base}^{step}\t{pows}\t", end="")
        pows %= z
        print(f"{pows}\t", end="")
        if y & 1:
            print("1\t", end="")
            counter_mp+=1
            ost = (ost * pows)
            if counter == 0:
                print(" \t", end="")
            else:
                print(f"{ost}\t", end="")
            ost %= z
            print(f"{ost}", end="")
        else:
            print("0\t-\t-", end="")
        print("")
        pows *= pows
        y >>= 1
        step *= 2
        counter += 1   
    print()
    print(f"Result is {ost}")
    print(f"Number of multiplications {counter_mp}")





power(5, 701, 11)
print("проверка через pow", pow(5,701,11))
power(2,2421,47)
print("проверка через pow",pow(2,2421,47))
power(7,5474,13)
print("проверка через pow",pow(7,5474,13))
