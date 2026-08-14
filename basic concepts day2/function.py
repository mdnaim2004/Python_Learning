"""
void name(){
    return 0;   // in c/c++ program
}
"""

# in python

def duble_it(num):
    res = num*2
    print(res)
    return res
duble_it(8)


def sum(num1, num2):
    result = num1+num2
    return result

total = sum(33, 45)
print("the result is = ",total)

final = duble_it(total)
print("Final Value = ", final)