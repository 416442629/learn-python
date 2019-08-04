def displayRange(lower,upper):
    while lower<=upper:
        print(lower)
        lower=lower+1
def displayRange2(lower,upper):
    if lower<=upper:
        print(lower)
        displayRange2(lower+1,upper)
displayRange(1,10)
displayRange2(12,20)