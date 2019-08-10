#递归
def ourSum(lower,upper):
    if lower > upper:
        return 0
    else:
        return lower+ourSum(lower+1,upper)


print(ourSum(3,6))