#嵌套函数
def factorialOne(n):
    def recurse(n,product):
        if n==1:
            return product
        else:
            return recurse(n-1,n*product)
    return recurse(n,2)
def factorial(n,product):
    print(n,product)
    if n == 1:
        return product
    else:
        return factorial(n - 1, n * product)



print(factorial(10,1))
print('-----------')
print(factorialOne(10))
