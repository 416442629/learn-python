#递归调试+理解递归
def ourSum(lower,upper,margin=0):
    blanks='-' *margin
    print(blanks,lower,upper,margin)
    if lower>upper:
        print(blanks,'这呢')
        return 0
    else:
        result=lower+ourSum(lower+1,upper,margin+4)
        print(blanks,result)
        return result


print('end:',ourSum(1,6))